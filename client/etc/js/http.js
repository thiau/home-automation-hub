function init(resolve, reject) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState === 4) {
            if (xhttp.status >= 200 && xhttp.status < 400) {
                if (xhttp.responseText || xhttp.response === "") {
                    try {
                        resolve(JSON.parse(xhttp.responseText));
                    } catch (e) {
                        resolve(xhttp.responseText);
                    }
                } else {
                    reject("Empty response");
                }
            } else {
                if (!xhttp.status && !xhttp.responseText) {
                    reject({
                        status: 0,
                        message: "Server not reachable and/or offline.",
                    });
                } else {
                    reject({
                        status: xhttp.status,
                        message: xhttp.responseText,
                    });
                }
            }
        }
    };
    return xhttp;
}

function setHeaders(xhttp, opts = {}) {
    if (opts && opts.contentType) {
        xhttp.setRequestHeader("Content-Type", opts.contentType);
    } else {
        xhttp.setRequestHeader("Content-Type", "application/json");
    }

    if (opts.headers) {
        (opts.headers || []).forEach((header) =>
            xhttp.setRequestHeader(header.key, header.value)
        );
    }
    return xhttp;
}

export default class HttpRequest {

    get (url, opts) {
        return new Promise(function (resolve, reject) {
            if (window.XMLHttpRequest) {
                let xhttp = init(resolve, reject);
                xhttp.open("GET", url);
                setHeaders(xhttp, opts).send();
            } else {
                reject("AJAX Calls not supported on this browser");
            }
        });
    }
}
