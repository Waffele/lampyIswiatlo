{*
* 2019-2021 gamiphy
*
* Gamiphy OF LICENSE
*
* Gamiphy License
*
* DISCLAIMER
*
* Do not edit or add to this file
*
*  @author    Gamiphy
*  @copyright 2019-2021 Gamiphy
*  @license   Gamiphy
*}

{literal}
<script src="{/literal}{$gamiphy_js_url|escape:'javascript':'UTF-8'}{literal}"></script>
<script type="text/javascript">
    window.addEventListener('load', () => {
        if (window.Gamiphy) {
            window.Gamiphy.init({
                app: "{/literal}{$gamiphy_app_id|escape:'javascript':'UTF-8'}{literal}",
                {/literal}
                    {if $gamiphy_customer_id}
                {literal}
                user: {
                    externalId: "{/literal}{$gamiphy_customer_id|escape:'javascript':'UTF-8'}{literal}",
                    email: "{/literal}{$gamiphy_customer_email|escape:'javascript':'UTF-8'}{literal}",
                    firstName: "{/literal}{$gamiphy_customer_firstname|escape:'javascript':'UTF-8'}{literal}",
                    lastName: "{/literal}{$gamiphy_customer_lastname|escape:'javascript':'UTF-8'}{literal}",
                    hash: '{/literal}{$gamiphy_hash|escape:'javascript':'UTF-8'}{literal}',
                },
                {/literal}
                    {/if}
                {literal}
                goToAuth: (isSignUp) => {
                    if(isSignUp) {
                        window.location.href = '/login?create_account=1'
                    } else {
                        window.location.href = '/login'
                    }
                },
                visible: !window.location.href.includes('/login'),
                currency: {
                    code: '{/literal}{$gamiphy_currency_iso|escape:'javascript':'UTF-8'}{literal}',
                    exchangeRate: {/literal}{$gamiphy_currency_conversion_rate|escape:'javascript':'UTF-8'}{literal}
                }
            });
            {/literal}
            {if $gamiphy_product_id}
            {literal}
                window.Gamiphy.showProductNotification("{/literal}{$gamiphy_product_id|escape:'javascript':'UTF-8'}{literal}");
            {/literal}
            {/if}
            {literal}
        }
    });
</script>
{/literal}