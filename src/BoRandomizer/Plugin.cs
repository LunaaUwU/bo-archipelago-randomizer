using BepInEx;
using BepInEx.Logging;

namespace BoRandomizer;

[BepInPlugin(PluginGuid, PluginName, PluginVersion)]
public class Plugin : BaseUnityPlugin
{
    public const string PluginGuid = "luna.bo.randomizer";
    public const string PluginName = "Archipelago Randomizer";
    public const string PluginVersion = "0.0.1";
    internal static new ManualLogSource Logger;

    private void Awake()
    {
        // Plugin startup logic
        Logger = base.Logger;
        Logger.LogInfo($"Plugin {PluginGuid} is loaded!");
    }
}
