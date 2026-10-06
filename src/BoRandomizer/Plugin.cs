using BepInEx;
using BepInEx.Logging;
using HarmonyLib;

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
        Harmony.CreateAndPatchAll(typeof(Plugin));
        Logger = base.Logger;
        Logger.LogInfo($"Plugin {PluginGuid} is loaded!");
    }

    //[HarmonyPatch(typeof(Narrator), "AfterNarration")]
    //[HarmonyPostfix]
    //static void InterceptAbilityUnlock(Narrator.NarratorState ___currentState)
    //{
    //    if (___currentState == Narrator.NarratorState.Staff)
    //    {
    //        Logger.LogInfo("Intercepting Equinox Staff unlock");
    //        GameManager.Instance.abilityManager.CanAttack = false;
    //        GameManager.Instance.inventoryContainer.Kitsunebi += 30;
    //        UICache.Instance.KitsunebiWiggle.AnimateKitsunebiIcon();
    //        UICache.Instance.KitsunebiWiggle.KitsunebiAchievementCalculation(30);
    //    }
    //}

    [HarmonyPatch(typeof(Kodamas), "PickKodama")]
    [HarmonyPrefix]
    static bool InterceptKodama(Kodamas __instance, ref SaveGameObject ___saveGameObject)
    {
        string kodamaId = "";
        if (___saveGameObject != null)
            kodamaId = ___saveGameObject.LegacySavedID;
        Logger.LogInfo($"Kodama with Id {kodamaId} collected");

        if (kodamaId == "Intro New kodamaCBF Intro975.255668.958070")
        {
            GameManager.Instance.abilityManager.CanAttack = false;
            GameManager.Instance.inventoryContainer.Kitsunebi += 30;
            UICache.Instance.KitsunebiWiggle.AnimateKitsunebiIcon();
            UICache.Instance.KitsunebiWiggle.KitsunebiAchievementCalculation(30);
        }
        return true;
    }

    [HarmonyPatch(typeof(NewPlayer), "Start")]
    [HarmonyPostfix]
    static void EarlyAbilities()
    {
        if (!GameManager.Instance.abilityManager.CanAttack || !GameManager.Instance.abilityManager.CanDash ||
            !GameManager.Instance.abilityManager.CanWallJump || !GameManager.Instance.abilityManager.CanIDash ||
            !GameManager.Instance.abilityManager.CanHover)
        {
            Logger.LogInfo("Early Abilities Given");
            GameManager.Instance.abilityManager.CanAttack = true;
            GameManager.Instance.abilityManager.CanDash = true;
            GameManager.Instance.abilityManager.CanWallJump = true;
            GameManager.Instance.abilityManager.CanIDash = true;
            GameManager.Instance.abilityManager.CanHover = true;
        }
    }

}
