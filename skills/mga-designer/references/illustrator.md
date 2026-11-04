# Illustrator setup and drawing

## Connect a desktop Illustrator session

Use a local desktop session with Adobe Illustrator installed and licensed, an MCP client and a supported Node.js runtime. The upstream npx instructions require Node.js 20 or newer. Check the current upstream support notes and the installed Illustrator version. An older installation or a working server handshake still needs a real drawing test. Record the server version separately from the Illustrator version. [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server) · [npm package](https://www.npmjs.com/package/illustrator-mcp-server)

1. Identify the user's platform and available MCP host. Inspect its registered servers and live tools, e.g. `codex mcp list` in Codex. Reuse a working entry even if it uses a different name. If installation is needed, use the upstream package and configure one transport. Installing the MGA-Designer skill provides workflow instructions. The Illustrator server is a separate dependency.
2. For a host that supports stdio, register the command below using that host's own configuration. The example pins upstream package version 1.10.3 for reproducibility. When changing versions, check the new package and repeat the drawing test. A host with generic JSON settings may accept the example below. Codex and Claude Code provide CLI equivalents.

```json
{
  "mcpServers": {
    "illustrator": {
      "command": "npx",
      "args": ["-y", "illustrator-mcp-server@1.10.3"]
    }
  }
}
```

```sh
# Codex on macOS or another host able to execute npx directly
codex mcp add illustrator -- npx -y illustrator-mcp-server@1.10.3

# Codex on Windows where npx is a batch launcher
codex mcp add illustrator -- cmd /d /c npx -y illustrator-mcp-server@1.10.3

# Claude Code on a host able to execute npx directly
claude mcp add illustrator -- npx -y illustrator-mcp-server@1.10.3
```

   Choose the single command that matches the host. If npx cannot be located from the desktop client, find the installed executable or install the pinned package in a dedicated tools directory with `npm install --save-exact illustrator-mcp-server@1.10.3`. Configure the host to execute the absolute Node executable and pass the absolute installed `node_modules/illustrator-mcp-server/dist/index.js` as its argument. A stdio-capable SDK client on the same desktop can connect to that server when the host cannot register it directly. In all cases discover the tools after connecting. Claude Desktop also supports the upstream packaged extension. Reconnect or restart the client if required by its configuration.
3. Start or select the intended Illustrator instance. On macOS, review the local Automation permission if desktop control is denied. On Windows, the upstream bridge requires a usable desktop Illustrator COM session. A remote host or headless environment needs a working connection to the desktop machine. Do not infer cross-platform compatibility from one test.

## First-run drawing test

Use a fresh output directory and absolute file names. Open a new disposable artboard, leaving the user's existing documents alone. Discover the live names and input schemas through the client's tools list. In SDK clients use `listTools` and `callTool`. The sequence below names the upstream operations and illustrates key arguments in version 1.10.3. Replace paths with the actual new output paths before calling.

| Action | MCP operation and example arguments |
|---|---|
| Start a blank RGB document | `create_document` with `{"width":400,"height":225,"color_mode":"rgb"}` |
| Name a layer | `manage_layers` with `{"action":"add","layer_name":"Probe"}` |
| Draw a vector | `create_path` with `{"anchors":[{"x":25,"y":80},{"x":100,"y":80},{"x":100,"y":110}],"closed":true,"fill":{"type":"rgb","r":40,"g":99,"b":130},"layer_name":"Probe"}` |
| Add live text | `create_text_frame` with `{"x":25,"y":40,"contents":"Editable test 2","font_size":18,"layer_name":"Probe"}` |
| Save, close and reopen | `save_document` with `mode: "save_as"` and a new absolute AI `path`. Check the result and file, then close **only the disposable document** and use `open_document` with the saved AI path. |
| Inspect the reopened master | `get_document_info`, `get_document_structure` and `list_text_frames`. Check that the intended layer, a path and the exact editable text survived. |
| Export and view | `export` with `target: "artboard:0"`, `format: "png"` and an absolute `output_path`. Open the returned or on-disk PNG in a viewer and look for the shape and text. Use the actual reported export name. |

Record OS, application and server versions, transport, checks performed and any error text. An MCP result may contain an error even when the process exits successfully. Inspect the returned status and output file. On a slow Windows cold start, wait until Illustrator's main window responds, then retry a read-only call before diagnosing a bridge failure. If a call times out after saving or drawing, inspect the open document and file before retrying to avoid duplicate objects. Use sequential modifications in a shared desktop session.

**Verified v1.0 setup.** On a Windows desktop with Node 24.16.0 and Illustrator 2023 (27.5.0), the unmodified 1.10.3 npm server over local stdio created a named layer, native path and live text, saved and reopened the AI, and exported PNG, SVG and PDF. A cold font query timed out before Illustrator finished starting. The same query succeeded after its window was ready. The SVG exporter included the artboard name in the output filename. Check the returned path.

## Draw the approved figure

- Set the artboard in the correct physical dimensions. Confirm the server's coordinate convention and units. Draw one scene first, export it and inspect it before repeating its visual language across the figure.
- Establish layers for the major conceptual modules, connections, labels and quantitative marks. Use the actual scene or action to link samples, tests and derived measures. Add short labels to connect those measurements to the comparison. Make a reader's path end at the takeaway.
- Draw via the advertised MCP path, text and layer tools. An original vector component may be imported via an editable SVG operation if the installed server supports it. Inspect the resulting object hierarchy. If the component is a single placed or rasterized image, recreate or import it as editable geometry before claiming editable artwork.
- Before importing a locally generated SVG, check that every numeric path argument is finite (including the final point), then reopen the AI in Illustrator and compare its clipping and fills with the approved preview.
- Put quantitative marks on a defined scale. Calculate positions from the actual estimates and intervals. A schematic curve must be identified as schematic and visually separated from measured data. Keep live text in the master if an export requires outlined text.
- Save to a new AI file. Export the PNG and the vector PDF (via the advertised PDF export operation) from the approved artboard. Apply journal-specific settings when supplied. Verify output paths, including artboard suffixes added by the application.

## If the bridge fails

Locate the failure first: server startup, MCP registration, application access, write, save/reopen or export. Inspect the error, actual Illustrator instance, supported tools, target path and any previous partial output. Retry a recoverable failure through MCP after confirming the target. Keep completed design records available to the author.

If direct native scripting would be needed, state the failed operation, the exact step that a native Illustrator script would perform, what would remain editable and which checks would still be possible. **Wait for explicit agreement** before switching to JSX, direct Windows COM or AppleScript to perform the work outside the MCP server, including a mixed workflow. If the user declines, deliver the completed design proposal and indicate which artwork files are pending. Record the actual route in the report. A renamed SVG or flattened preview cannot fulfill delivery of a layered AI master.
