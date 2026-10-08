using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Packets;
using System;
using System.Collections.Concurrent;
using Archipelago.MultiClient.Net.Helpers;

namespace BoRandomizer
{
    public class ArchipelagoClient
    {
        private static ArchipelagoSession _session;

        public static ConcurrentQueue<string> _itemQueue { get; } = new ConcurrentQueue<string>();

        public static void Connect(string server, string port, string user, string pass = "")
        {
            Plugin.Log.LogInfo($"Attempting connection to archipelago at server: {server}:{port} as {user}");
            _session = ArchipelagoSessionFactory.CreateSession(server, Int32.Parse(port));
            _session.Items.ItemReceived += OnItemReceived;
            LoginResult result;
            try
            {
                result = _session.TryConnectAndLogin("Bo", user, ItemsHandlingFlags.AllItems, new Version(0, 6, 7), null, null, pass);
            }
            catch (Exception e)
            {
                result = new LoginFailure(e.GetBaseException().Message);
            }

            if (!result.Successful)
            {
                LoginFailure failure = (LoginFailure)result;
                string errorMessage = $"Failed to Connect to {server} as {user}:";
                foreach (string error in failure.Errors)
                {
                    errorMessage += $"\n    {error}";
                }
                foreach (ConnectionRefusedError error in failure.ErrorCodes)
                {
                    errorMessage += $"\n    {error}";
                }
                Plugin.Log.LogError(errorMessage);
                return;
            }
            Plugin.Log.LogInfo("Connected successfully");

            var loginSuccess = (LoginSuccessful)result;
        }

        public static void SendLocationCheck(long locationId)
        {
            if (!IsConnected())
            {
                Plugin.Log.LogWarning($"Cannot send check {locationId}: Not connected to server");
                return;
            }

            if (_session.Locations.AllLocationsChecked.Contains(locationId))
            {
                Plugin.Log.LogInfo($"Location {locationId} was already checked");
                return;
            }

            _session.Locations.CompleteLocationChecks(locationId);
            Plugin.Log.LogInfo($"Sent location check ID: {locationId}");
        }

        public static void SendVictory()
        {
            if (!IsConnected())
                return;
            var statusUpdate = new StatusUpdatePacket()
            {
                Status = ArchipelagoClientState.ClientGoal
            };
            _session.Socket.SendPacketAsync(statusUpdate);
            Plugin.Log.LogInfo("Sent victory status packet to server");
        }

        private static void OnItemReceived(ReceivedItemsHelper helper)
        {
            var item = helper.DequeueItem();
            string itemName = _session.Items.GetItemName(item.ItemId);
            Plugin.Log.LogInfo($"Received {itemName}. Adding to queue");

            _itemQueue.Enqueue(itemName);
        }

        public static bool IsConnected()
        {
            return !(_session == null || !_session.Socket.Connected);
        }

        public static bool HasReceivedItem(string itemName)
        {
            if (!IsConnected())
                return false;

            foreach (var item in _session.Items.AllItemsReceived)
            {
                string receivedName = _session.Items.GetItemName(item.ItemId);
                if (receivedName == itemName)
                    return true;
            }

            return false;
        }
    }
}
