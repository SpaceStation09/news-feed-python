# News feed (python version)

[![smithery badge](https://smithery.ai/badge/@SpaceStation09/news-feed-python)](https://smithery.ai/server/@SpaceStation09/news-feed-python)

使用[`fastmcp`](https://gofastmcp.com/getting-started/quickstart)工具，进行mcp server的开发，提供 blockbeats rss的data feed给大模型，以完成用户对于咨询查询的回答。

## 启动

### Installing via Smithery

To install News Feed Python Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@SpaceStation09/news-feed-python):

```bash
npx -y @smithery/cli install @SpaceStation09/news-feed-python --client claude
```

### Installing Manually
安装依赖

``` bash
uv pip install -r requirements.txt 
```

启动http 监听

```bash
uv run ./news-feed.py
```

## Testing

可以使用[`mcp-inspector`](https://github.com/modelcontextprotocol/inspector)提供的ui来测试mcp的功能：

```bash
npx @modelcontextprotocol/inspector
```

启动后，终端会print出可以访问的http link，在浏览器中访问该link。

然后可以启动mcp server：

```bash
uv run ./news-feed.py
```

server此时可通过 http 被链接：`http://127.0.0.1:8000/mcp/`，你可以在上一步中的ui中通过 streamable HTTP的方式去连接到mcp 并进行测试。

## Future Work

- [ ] ASGI Integration
