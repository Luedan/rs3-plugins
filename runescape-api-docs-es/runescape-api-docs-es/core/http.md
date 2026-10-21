# HTTPRequest

## Descripción General

In some cases it may be useful for plugins to retrieve additional data on-demand from an external source, rather than bundling the data with the plugin, or to send data to an external location.

Plugins can make use of the HTTPRequest type to perform `GET` and `POST` requests, allowing them to retrieve and send data if needed.

## Requirements

To ensure safety and prevent misuse, plugins must request the `httpAccess` permission in their manifest in order to be able to create or trigger HTTPRequests, like so:

```json
"requiredPermissions": [ "httpAccess" ],
    "optionalPermissions": [],
```

Additionally, the URLs that will be used must also be specified in the manifest, however you just need to specify the base URLs instead of all endpoints:

```json
"urls": { "wiki" : "http://www.runescape.wiki" },
```

> **Advertencia**
> Specifying malformed URLs or URL shortener/redirect addresses will cause your plugin to be rejected.

## Ejemplo

```json
"requiredPermissions": [],
    "optionalPermissions": [ "httpAccess" ],
    "urls": { "wiki" : "http://www.runescape.wiki" },
```

```lua
-- Callback triggered when an HTTP request finishes
    local function RequestResultHandler(request)
        if request.successful then
            log("Response code=", request.responseCode,
                "got header of length", string.len(request.header),
                "and response data of length", string.len(request.data))
            -- Process request.data
        elseif request.timedOut then
            log(request.url, "request timed out")
        elseif request.failed then
            log(request.url, "request failed, error code =", request.errorCode)
        end
    end

    -- Only do anything if we have permission
    if Plugin.HasPermission(PluginPermissions.httpAccess) then
        -- Search the wiki
        local searchString = "cat"
        local urlPath = formatStr("/api.php?action=query&format=json&list=search&formatversion=2&srsearch={}", searchString)

        HTTPRequest.new(Plugin.urls.wiki, urlPath):Get(RequestResultHandler)
    end
```

## Métodos

### Constructor

```lua
function HTTPRequest.new(baseURL : PluginURL, path : String?) -> HTTPRequest
```

Creates a request pointing at a combination of the baseURL and an optional path.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| baseURL | [PluginURL](./plugin.md#urls) | Base URL address to concatenate `path` to.    Specified in the manifest and accessed via the `Plugin.urls` table. |
| path | String? | Optional additional path to concatenate to the baseURL. |

> **Ejemplo**
> ```lua
> HTTPRequest.new(Plugin.urls.wiki, "index.html?bla=100")
> ```

### Get/Post

```lua
function HTTPRequest:Get(
    completionCallback : function? (self : HTTPRequest),
    progressCallback : function? (self : HTTPRequest))

function HTTPRequest:Post(
    data : String,
    completionCallback : function? (self : HTTPRequest),
    progressCallback : function? (self : HTTPRequest))
```

Triggers a `GET`/`POST` request to the remote endpoint specified by this request, and optionally sets up callbacks to track its completion and/or progress.

> **Advertencia**
> Calling this method on an active request will trigger an error.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| completionCallback | function? (self : HTTPRequest) | Callback triggered when this request finishes, regardless of success.    Receives this request as its parameter. |
| progressCallback | function? (self : HTTPRequest) | Callback triggered whenever this request's download progress changes.    Receives this request as its parameter. |

> **Ejemplo**
> ```lua
> local function RequestResultHandler(request)
>     print("ok=", request.successful)
> end
> 
> local function RequestProgressHandler(request)
>     print("progress=", request.progress)
> end
> 
> if Plugin.HasPermission(PluginPermissions.httpAccess) then
>     HTTPRequest.new(Plugin.urls.wiki):Get(RequestResultHandler, RequestProgressHandler)
> end
> ```

### Cancel

```lua
function HTTPRequest:Cancel()
```

### AddHeader

```lua
function HTTPRequest:AddHeader(key : String, value : String)
```

> **Advertencia**
> Calling this method on an active request will trigger an error.

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| data | String | Contains the response received from the remote server, or an empty string if the request is pending or has failed. |
| header | String | Contains the header received from the remote server, or an empty string if the request is pending or has failed. |
| cancelled | Bool | Indicates whether this request has been cancelled by the user. |
| finished | Bool | Indicates whether this request has been completed, regardless of whether it succeeded or not. |
| successful | Bool | Indicates whether this request has been completed successfully. |
| failed | Bool | Indicates whether this request has failed due to an error. |
| timedOut | Bool | Indicates whether this request has failed due to not getting a response from the specified target. |
| responseCode | Int | HTTP response code received from the target. |
| errorCode | Int | HTTP error code received from the target. |
| errorInfo | String | If `failed` is true, this contains additional information regarding the cause of the error. |
| progress | Float? | Returns a value in a 0..1 range representing the download progress for this request.    If the server does not provide expected download size information, this is instead nil. |
| url | String | The address this request is attempting to communicate with. |
| downloadedBytes | Int | Number of bytes downloaded from the target so far. |
| downloadTotalBytes | Int | Number of bytes expected to be downloaded from the target.    Note in some cases this may be 0 despite an in-progress download, as some servers do not provide the necessary information. |