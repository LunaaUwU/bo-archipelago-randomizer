using System;
using System.Collections.Generic;
using System.Text;
using UnityEngine;

namespace BoRandomizer
{
    public class ItemProcessor : MonoBehaviour
    {
        public static void ProcessItem(string itemName)
        {
            switch (itemName)
            {
                case "equinox_staff":
                    GameManager.Instance.abilityManager.CanAttack = true;
                    break;

                case "fox_fire_30":
                    GameManager.Instance.inventoryContainer.Kitsunebi += 30;
                    UICache.Instance.KitsunebiWiggle.AnimateKitsunebiIcon();
                    UICache.Instance.KitsunebiWiggle.KitsunebiAchievementCalculation(30);
                    break;
            }
        }
    }
}
