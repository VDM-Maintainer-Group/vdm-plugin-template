# Plugin Development Norm

> For Virtual Domain Manager v1.0.0

### Develop Procedure

1. **Repo Init**: use `npm init` for convenience, or copy and modify an existing `package.json`.
2. **Dependency Claim**: the capability dependency should be firstly described in `package.json` file, then the safety of RPC calling of capacity function in your plugin is promised. For other dependencies, please include them in your repo or install via `pre-install` script in `package.json`.
3. **Plugin Test**: use `zip` to archive your plugin repo firstly, and use `pyvdm plugin install <*.zip file>` to install; then, use `pyvdm plugin run <func>` to apply unit test.
4. **Plugin Publish**: (not implemented)
