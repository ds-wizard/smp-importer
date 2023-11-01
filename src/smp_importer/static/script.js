const importer = new DSWImporter()

importer
    .init({
        useWizardStyles: true,
        windowSize: {
            width: 600,
            height: 500,
        },
    })
    .then(() => {
        jQuery('#file-input').on('input', function (e) {
            const files = e.target.files
            console.log(files)
            loadFile(files[0])
        })

        jQuery('#btn-github-load').on('click', function () {
            const owner = jQuery('#github-owner-input').val()
            const repo = jQuery('#github-repo-input').val()
            const file = jQuery('#github-file-input').val()
            console.log(`${owner}/${repo}:/${file}`)
            loadGitHubPublic(owner, repo, file)
        })

        jQuery('#btn-url-load').on('click', function () {
            const url = jQuery('#url-input').val()
            console.log(url)
            loadUrl(url)
        })
    })
    .catch(error => {
        console.error(error)
    })


function isValidUrl(urlString) {
    const urlPattern = new RegExp('^(https?:\\/\\/)?'+ // validate protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // validate domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))'+ // validate OR ip (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // validate port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?'+ // validate query string
        '(\\#[-a-z\\d_]*)?$','i') // validate fragment locator
    return !!urlPattern.test(urlString)
}

function doImport(actions) {
    const replacements = new Map()
    const debug = jQuery('#debug-checkbox').is(':checked')
    console.log(actions)

    const replacePath = (path) => {
        let newPath = [];
        path.forEach((pathItem) => {
            if (replacements.has(pathItem)) {
                newPath.push(replacements.get(pathItem))
            } else {
                newPath.push(pathItem)
            }
        })
        return newPath
    }

    actions.forEach((item) => {
        if (item.type === 'debug') {
            console.log('DEBUG:', item.message)
        } else if (item.type === 'setReply') {
            const path = replacePath(item.path)
            console.log(`SET REPLY: ${path} = "${item.value}"`)
            importer.setReply(path, item.value)
        } else if (item.type === 'setIntegrationReply') {
            const path = replacePath(item.path)
            console.log(`SET INTEGRATION REPLY: ${path} = "${item.value}" [${item.itemId}]`)
            importer.setIntegrationReply(path, item.value, item.itemId)
        } else if (item.type === 'addItem') {
            const path = replacePath(item.path)
            const itemUuid = importer.addItem(path)
            console.log(`ADD ITEM: ${path} = ${itemUuid} [${item.var}]`)
            replacements.set(item.var, itemUuid)
        }
    })

    if (debug) {
        alert('Stop (debug enabled)')
    }

    importer.send()
}

function loadUrl(url) {
    if (!isValidUrl(url)) {
        alert('Invalid URL!')
        jQuery('#url-input').val('')
    } else {
        jQuery.ajax({
            type: 'POST',
            url: `/api/import-url`,
            data: JSON.stringify({'url': url}),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (result) {
                doImport(result.actions)
            },
            error: function (result) {
                console.log(result)
                alert('failed')
            }
        })
    }
}

function loadFile(file) {
    const reader = new FileReader()
    reader.addEventListener('load', (event) => {
        let data = ''
        try {
            data = event.target.result
        } catch (error) {
            alert('Failed to load file')
        }

        jQuery.ajax({
            type: 'POST',
            url: `/api/import-file`,
            data: JSON.stringify({
                'contents': data,
                'type': file.type,
                'name': file.name,
                'bytesize': file.size,
            }),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (result) {
                doImport(result.actions)
            },
            error: function (result) {
                console.log(result)
                alert('failed')
            }
        })
    })
    reader.readAsText(file)
}

function loadGitHubPublic(owner, repo, file) {
    jQuery.ajax({
            type: 'POST',
            url: `/api/import-github-public`,
            data: JSON.stringify({
                'owner': owner,
                'repo': repo,
                'file': file,
            }),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (result) {
                doImport(result.actions)
            },
            error: function (result) {
                console.log(result)
                alert('failed')
            }
        })
}

