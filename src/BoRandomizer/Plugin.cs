using BepInEx;
using BepInEx.Logging;
using FMOD.Studio;
using HarmonyLib;
using UnityEngine;

namespace BoRandomizer;

[BepInPlugin(PluginGuid, PluginName, PluginVersion)]
public class Plugin : BaseUnityPlugin
{
    public const string PluginGuid = "luna.bo.randomizer";
    public const string PluginName = "Archipelago Randomizer";
    public const string PluginVersion = "0.0.1";
    internal static new ManualLogSource Log;

    private Harmony harmony = null!;
    public static Plugin Instance = null!;

    private void Awake()
    {
        Log = Logger;
        DontDestroyOnLoad(gameObject);
        Harmony.CreateAndPatchAll(typeof(Plugin));
        
        Log.LogInfo($"Plugin {PluginGuid} is loaded!");

        ArchipelagoClient.Connect("localhost", "38281", "Luna");
    }

    private void Update()
    {
        if (!ArchipelagoClient.IsConnected())
            return;

        if (ArchipelagoClient._itemQueue.IsEmpty)
            return;

        if (GameManager.Instance.Player == null)
            return;

        if (ArchipelagoClient._itemQueue.TryDequeue(out string itemName))
        {
            Plugin.Log.LogInfo($"Processing queued item: {itemName}");
            ItemProcessor.ProcessItem(itemName);
        }
    }

    [HarmonyPatch(typeof(Narrator), nameof(Narrator.AfterNarration))]
    [HarmonyPostfix]
    static void InterceptAbilityUnlock(Narrator.NarratorState ___currentState)
    {
        if (!ArchipelagoClient.IsConnected())
            return;

        if (___currentState == Narrator.NarratorState.Staff)
        {
            ArchipelagoClient.SendLocationCheck(1);
            GameManager.Instance.abilityManager.CanAttack = ArchipelagoClient.HasReceivedItem("equinox_staff");
        }
    }

    [HarmonyPatch(typeof(Kodamas), nameof(Kodamas.PickKodama))]
    [HarmonyPrefix]
    static bool PickKodama(Kodamas __instance, ref SaveGameObject ___saveGameObject, ref NewPlayer ___player, ref bool ___active,
                                ref LinkedMapIcon ___linkedMapIcon, ref Animator ___animator, ref ParticleSystem ___particle,
                                ref GameObject ___uiIndicator, ref EventInstance ___kodamaIdleInstance)
    {
        if (!ArchipelagoClient.IsConnected())
            return true;

        string kodamaId = "";
        if (___saveGameObject != null)
            kodamaId = ___saveGameObject.LegacySavedID;
        Log.LogInfo($"Kodama with Id {kodamaId} collected");

        if (kodamaId == "Intro New kodamaCBF Intro975.255668.958070" && !___active)
        {
            ___player.PickingKodama = true;
            if(___linkedMapIcon != null)
                ___linkedMapIcon.DisableLinkedIcon();
            ___animator.cullingMode = AnimatorCullingMode.AlwaysAnimate;
            ___active = true;
            ___particle.Stop();
            ___player.animator.SetTrigger("PickKodama");
            ___animator.Play("kodamaPulling");
            ___player.ResetVelocity();
            ___uiIndicator.SetActive(false);
            SFX.StopAndReleaseInstanceFadeOut(___kodamaIdleInstance);

            ArchipelagoClient.SendLocationCheck(2);
            return false;
        }
        return true;
    }

    [HarmonyPatch(typeof(AsahiIntro), nameof(AsahiIntro.Crafting))]
    [HarmonyPostfix]
    static void UpgradeStaff(AsahiIntro __instance)
    {
        if (!ArchipelagoClient.IsConnected())
            return;
        ArchipelagoClient.SendVictory();
    }

    //[HarmonyPatch(typeof(NewPlayer), nameod(NewPlayer.Start))]
    //[HarmonyPostfix]
    //static void EarlyAbilities()
    //{
    //    if (!GameManager.Instance.abilityManager.CanAttack || !GameManager.Instance.abilityManager.CanDash ||
    //        !GameManager.Instance.abilityManager.CanWallJump || !GameManager.Instance.abilityManager.CanIDash ||
    //        !GameManager.Instance.abilityManager.CanHover)
    //    {
    //        Logger.LogInfo("Early Abilities Given");
    //        GameManager.Instance.abilityManager.CanAttack = true;
    //        GameManager.Instance.abilityManager.CanDash = true;
    //        GameManager.Instance.abilityManager.CanWallJump = true;
    //        GameManager.Instance.abilityManager.CanIDash = true;
    //        GameManager.Instance.abilityManager.CanHover = true;
    //    }
    //}

}
