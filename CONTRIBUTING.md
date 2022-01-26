# Plugin Development Norm

> For Virtual Domain Manager <=v1.0.0

1. Create the `package.json` file use `npm init`, or copy and modifty an exiting file.
    ```json
    {
      "name": "",               // (required) your plugin name, both '-' and '_' allowed
      "version": "",            // (required) version number, e.g., "1.0.0"
      "description": "",        // (required) describe how this plugin support what application
      "keywords": [],           // (required) keywords for indexing
      "author": "",             // (optional) author name
      "license": "GPL-3.0",     // license claim

      "main": "",               // (required) entry file for the plugin, e.g., "main.js"
      "capability": [],         // (optional) VDM Capability depdency claim
      "scripts": {},            // (optional) now only "pre-install" and "test" are supported

      "homepage": "",           // (optional) homepage url for the plugin
      "repository": {},         // (optional) repository address for the plugin
      "bugs": {}                // (optional) bug report address for the plugin
    }
    ```

2. Write your plugin with `SRC` API implemented (`onTrigger` is not used now)
    - For Python version plugin, please refer [here](https://github.com/VDM-Maintainer-Group/virtual-domain-manager/blob/master/interface/__init__.py).
    - For CDLL version plugin, please refer [here](https://github.com/VDM-Maintainer-Group/virtual-domain-manager/blob/master/interface/src_api.h).

3. Archive your plugin with ".zip" format, and install it via pyvdm.
    ```bash
    zip -r ../plugin.zip ./
    pyvdm plugin install ../plugin.zip
    ```

4. Test your plugin functionality via pyvdm, or via your test script in `scripts` section
    ```bash
    pyvdm plugin run <your_plugin_name> <onStart/onStop/onClose>
    npm test
    ```

5. (Optional) Use **Github Action** to make your plugin available on release page, and submit to the offical `VDM Plugin Market` via PR.
    > The `VDM Plugin Market` has not been built up yet.

