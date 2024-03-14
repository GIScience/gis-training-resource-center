🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

(content:references:module9:ors-tools-plugin)=
# Plugin: Openrouteservice (ORS) tools

## Openrouteservice QGIS Plugin 

### Install the Plugin
-  Go under tab `Plugins`

```{figure} /fig/qgis_plugins.png
---
width: 700px
name: manage & install plugins
align: center
---
Where to manage and install plugins    Source: HeiGIT
```

-  Click on `Manage and install plugins`, a new window will open up
-  Search for "ORS Tools" in search line and click `Install plugin` (right bottom)

```{figure} /fig/install_ors.png
---
width: 700px
name: search ors tools plugin
align: center
---
How to install the ORS Tools plugin    Source: HeiGIT
```

-  Close the window
-  After a few seconds the plugin should appear under "Web" tab in QGIS as "ORS Tools"

```{figure} /fig/open_ORS_tools_plugin.png
---
width: 700px
name: locate ors tools plugin in qgis
align: center
---
Where to open the ORS Tools plugin    Source: HeiGIT
```
-  Open the "ORS tools" plugin - click on the ORS Tolls icon in the toolbar <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/icon_ORS_tools_plugin.png" alt="Icon" width="20" height="20">
-  To make use of the ORS tools, you first need to sign up. Therefore click `Sign Up`

```{figure} /fig/signup_ORS.png
---
width: 700px
name: basic classification
align: center
---
Where to sign up for OpenRouteService    Source: HeiGIT
```
### Sign up and setup
-  You will be redirected to the Openrouteservice site, where you need to create     a user account
  
```{figure} /fig/sign_up_ORS.png
---
width: 700px
name: sign up for ors
align: center
---
How to sign up for Openrouteservice    Source: HeiGIT
```

-  After submitting your profile, a confirmtaion e-mail will be sent to your mail    adress
-  Please confirm your account
-  You are now able to create tokens (API keys) which allow you to run queries through the ORS Tools plugin in QGIS
-  Click into the field under "Request a token" and choose "Free"
-  Choose a "Token Name" in the field to the right and "Create token"
-  The token will directly appear above in the "key" field

```{figure} /fig/ORS_token.png
---
width: 700px
name: generate key
align: center
---
How to create a token (API key)    Source: HeiGIT
```
-  Click on the token, it will directly be copied. You can now go back into QGIS     for further setup

### Configure the plugin

-  In QGIS and go to `Provider Settings` in the ORS Tools window by clicking the settings icon (right next to „Provider field“)
-  Add the API key you just created into the „API Key“ field
-  Add URL: https://api.openrouteservice.org into the Base URL field
-  (Potentially: Click `Add` and enter „openrouteservice“ into the pop up window „Enter a name for the provider“)


```{figure} /fig/modul9_add_api.png
---
width: 350px
name: plugin config
align: center
---
Where to add API key     Source: HeiGIT

```

For further information: [https://github.com/GIScience/orstools-qgis-plugin]

