# P3 technology, dependency and license evaluation

Status: documentary research only, 2026-10-11. No package/runtime installed or adopted. [ADR-0002](../adr/ADR-0002-desktop-stack.md), [ADR-0003](../adr/ADR-0003-local-persistence.md), [ADR-0006](../adr/ADR-0006-authorized-browser.md) and [ADR-0007](../adr/ADR-0007-document-profiles.md) remain PROPOSED. Source retrieval verifies what a document says, not a release's compatibility, binary integrity or all transitive licenses.

## Evidence method and limitations
Fetched official upstream license/support documents using ordinary verified HTTPS; no authentication/credential values collected. Several official documentation hosts returned proxy tunnel 403; where possible consulted the vendor's own source repositories instead. Incorrect source paths returned 404 and corrected identifiable paths were retried; missing evidence remains explicit. No TLS/signature/checksum validation disabled. Retrieved text stored temporarily under `/tmp/p3-research`; stable SHA-256 and short conclusions below preserve source attribution without depending on that temporary cache. Source URLs using main/dev/master are moving snapshots, not package-version pins. Adoption requires release-tag-specific recheck, transitive/native/browser/font/tool licenses and exact Windows target.

## Alternatives and provisional direction
| Area / candidate | Assessment / tradeoff | Documentary evidence | Disposition |
| --- | --- | --- | --- |
| Modular monolith + workers | Local deployment/simple queue, independent modules; IPC/recovery and hard isolation complexity | P3 contract/design analysis | Preferred proposed architecture; P5 confinement/durability proof required |
| All in process | Lowest overhead but parser crash/resource fault can affect shell; hard containment weak | Design comparison | Not preferred for risky parsing/browser operations; pure domain helpers may remain in-process |
| Microservices/cloud/brokers | Unnecessary operational/runtime/network complexity; violates local-first constraints if compulsory | Master constraints | Rejected for initial product |
| .NET 10 + WPF | Native Windows UI/accessibility integration; one core language/platform, no webview for shell; supports declared OS table only | DOTNET10, DOTNET_POLICY, DOTNET_LICENSE, WPF | Preferred conditional desktop evaluation candidate ONLY on vendor-listed exact target; not adopted; absent owner OS info blocks selection |
| Python 3.13 + PySide/Qt | Strong file ecosystem, fewer browser-shell needs; bundling/performance/Qt license and native dependencies more complex | PYTHON_SOURCE/PYTHON_LICENSE, PYSIDE_SOURCE/QT_SOURCE; exact Qt table unavailable | Alternative conditional lane; binding/module licenses and pinned Qt OS support pending |
| Tauri v2 / Rust / WebView2 | Small app core but added Rust/web stack and runtime distribution/terms; no automatic minimal-total-footprint claim | RUST_WIN/RUST_LICENSE, TAURI_SOURCE/TAURI_LICENSE_SOURCE, WEBVIEW_OS | Conditional alternative; exact version/system/browser-runtime/license obligations unresolved |
| Electron | Consistent browser UI/tooling, heavier bundled Chromium/Node and update surface | ELECTRON_SOURCE/ELECTRON_LICENSE, NODE/NODE_LICENSE | Lower-priority candidate for minimal dependencies/resources; not rejected as inherently incompatible |
| Node.js | May be transitive browser-driver runtime, not necessary for a native desktop core | NODE main build table lists Windows 10/Server 2016 x64; NODE_LICENSE includes many dependency notices | No release pin/support claim; native/addon/runtime transitive review required |
| Rust | Candidate supervisor/native implementation, stronger typing but adds toolchain complexity if core differs | RUST_WIN says client Windows 10+; RUST_LICENSE one upstream license text | Exact release/toolchain/SDK and dual-license options/transitives pending |
| WebView2 | Windows distribution doc discusses Win10 runtime presence and Fixed Version deployment requirements; Microsoft runtime terms separate from sample-code license | WEBVIEW_OS; direct support page blocked, sample-license path unavailable | No verified blanket compatibility/free-redistribution approval; offline installer/runtime license/version review required |
| Playwright/.NET or JS | Rich browser evidence; driver/browser transitive runtime; current intro source lists Windows 11+, Server 2019+ or WSL | PLAYWRIGHT_DOTNET/INTRO and PLAYWRIGHT_LICENSE | Not supported evidence for native Windows 10 by current source; no workaround by silently pinning obsolete version or assuming WSL meets standalone requirement |
| Chromium | Browser engine useful for QA but main license not complete binary/third-party/licensing/support inventory | CHROMIUM_LICENSE | OS/browser/automation combination pending; installed cloud Chromium is irrelevant to owner Windows proof |
| Edge WebDriver/Selenium lane | Alternative browser QA architecture if current supported Win10 browser/driver can be evidenced | Not retrieved/verified here | Research-only fallback, NOT an adoption recommendation; hard scope control and supported versions must be proven |
| SQLite | Local embedded transactional storage, no service; single-writer fits initial queue | SQLITE_SOURCE distinguishes public-domain primary code and exceptions | Preferred candidate; provider/native wrapper/license/journal/durability proof pending |
| CsvHelper | Candidate explicit CSV parsing/writing/typed configuration | CSVHELPER dual MS-PL/Apache 2.0 | Choose permitted license branch after exact tag/transitives; no implicit locale/formula evaluation |
| ClosedXML | Candidate XLSX inspection/transforms; fidelity/formula evaluation limits | CLOSEDXML MIT | Not lossless-all-workbooks promise; version/transitive/font licenses and memory profile pending |
| Open XML SDK | Candidate DOCX placeholders/structured package access without Office runtime | OPENXML MIT | No native Word rendering/conversion fidelity promise; exact version/transitives pending |
| PDFsharp / PdfPig | Candidate PDF manipulation and digital text extraction respectively | PDFSHARP MIT / PDFPIG Apache 2.0 | Font/native/module features and redistribution assessed per selected package; OCR not provided by these claims |
| Tesseract local OCR | Possible future local OCR, language data/resources and quality limitations | TESSERACT Apache 2.0 | Outside approved initial detailed requirements; research-only extension requiring owner scope and P5 checks |
| HTML/JSON/CSV/ZIP reports | Local passive rendering/serialization/package capability; use core facilities when sufficient | Report design, no rendering library adopted | Preferred basic format proposals; PDF/XLSX rendering fidelity conditional |
| Inno Setup | Simple installer candidate; custom upstream license permits commercial use with retained notices/origin conditions | INNO, INNO_SOURCE | Binary distribution/current commercial access terms/Windows tool version not fully verified; no paid-license requirement adopted |
| WiX | MSI tooling flexibility, complexity and source reciprocal obligations | WIX MS-RL source text | Tool binaries/versions/business terms/extensions pending; no blanket free-current-binaries assumption |

## License obligations investigated
- MIT (.NET/WPF, ClosedXML, Open XML SDK, PDFsharp, Electron, Tauri source): retain copyright/permission notices in distributed substantial portions; exact selected package and third-party notices still need inventory.
- Apache 2.0 (Playwright, PdfPig, Tesseract; available CsvHelper branch; Rust source text): license/notice retention, modification notices as applicable and patent terms; inspect NOTICE files/derived packaging per exact version.
- MS-PL/Apache dual CsvHelper: source explicitly offers alternatives; selected compliance basis must be recorded, not silently combined.
- LGPL-3.0-only source texts for Qt/PySide: dynamic-link/relinkability, license/source/installation-information obligations depend on exact distribution, modifications and modules; compliance review required. No commercial license purchase is assumed necessary or approved; incompatible selected module/binary terms would block adoption.
- SQLite source states primary SQLite code is public domain but repository exceptions exist; wrapper/native package/test/tool licenses are separate. Do not label every bundled file public domain.
- Chromium BSD-style source text requires attribution and disclaimers; Chromium and Node distributions have third-party notices and licenses not covered by headline license. Browser binaries/codecs/assets require exact distribution review.
- Inno custom license: use/commercial use allowed in retrieved source, source/binary notices and modified/origin conditions; current compiled download/product terms not proven by that source alone.
- WiX MS-RL source obligations apply to covered files/modifications; actual compiler/binary/extension distribution and any fee conditions must be checked before selection.
- WebView2 proprietary runtime redistribution terms are not inferred from open-source samples. Windows/system fonts/native APIs are OS prerequisites, not redistributable open-source dependency claims; do not bundle fonts without rights.

No item has a complete version-pinned transitive SBOM, package signature verification or redistribution approval. NFR-0020 remains unverified; missing evidence blocks adoption, not honest documentary comparison.

## Required adoption record
Exact package/runtime/tool version and tag/commit, source URL, hash/signature/provenance, direct/transitive/native/browser/assets inventory, SPDX/license choice and obligations, cost/runtime restrictions, Windows edition/build/architecture table, offline packaging/update behavior, known advisories, maintainer lifecycle, P5 workload/fidelity/isolation evidence, owner ADR approval. No auto-updater/network fallback; locally imported verified update media planned in release design. Candidate score priorities: correctness/support/security/license first, then resources/maintenance/build simplicity; no invented benchmark scores.

## Source evidence register
FETCHED = read-only document retrieved; UNAVAILABLE = blocked/missing source, not a failed product test. Date 2026-10-11 for every entry. SHA below hashes exact response bytes; URLs are intentionally version-unpinned unless path says otherwise. Required source refresh/pin is documented above.
| Source ID | Authoritative URL | Retrieval | SHA-256 / limitation |
| --- | --- | --- | --- |
| WIN10 | [WIN10](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| DOTNET10 | [DOTNET10](https://raw.githubusercontent.com/dotnet/core/main/release-notes/10.0/supported-os.md) | FETCHED | 168f8bf76fdcaad9a1083ce5a96329291c17ef4c51e850b99c83f6e0457963f7 |
| WPF | [WPF](https://raw.githubusercontent.com/dotnet/wpf/main/LICENSE.TXT) | FETCHED | ae48df11a335dc1a615f4f938b69cba73bcf4485c4f97af49b38efb0f216353b |
| SQLITE | [SQLITE](https://www.sqlite.org/copyright.html) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| PLAYWRIGHT | [PLAYWRIGHT](https://playwright.dev/dotnet/docs/intro) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| PLAYWRIGHT_LICENSE | [PLAYWRIGHT_LICENSE](https://raw.githubusercontent.com/microsoft/playwright/main/LICENSE) | FETCHED | 45873d00a0dd243596deb4aa23b2493b3d1f0671921bf2538ea431d7380220eb |
| QT | [QT](https://doc.qt.io/qt-6/supported-platforms.html) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| PYSIDE | [PYSIDE](https://doc.qt.io/qtforpython-6/licenses.html) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| PYTHON | [PYTHON](https://docs.python.org/3.13/using/windows.html) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| TAURI | [TAURI](https://v2.tauri.app/start/prerequisites/) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| ELECTRON | [ELECTRON](https://www.electronjs.org/docs/latest/tutorial/windows-arm) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| NODE | [NODE](https://raw.githubusercontent.com/nodejs/node/main/BUILDING.md) | FETCHED | b3476baf699fbdb6d62b237e611e319342480e3d3b71f68d899c9fedddcd26c7 |
| RUST | [RUST](https://doc.rust-lang.org/rustc/platform-support.html) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| WEBVIEW2 | [WEBVIEW2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/supported-browsers) | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| CSVHELPER | [CSVHELPER](https://raw.githubusercontent.com/JoshClose/CsvHelper/master/LICENSE.txt) | FETCHED | 8444a77d74bd5e4f607222be36fb68b47986c73f318d374695a1055737a2f3c0 |
| CLOSEDXML | [CLOSEDXML](https://raw.githubusercontent.com/ClosedXML/ClosedXML/develop/LICENSE) | FETCHED | 3071658fba9a054edce74e756314ba926fe3ffe5c6622f209d21a0c8f1d2a99e |
| OPENXML | [OPENXML](https://raw.githubusercontent.com/dotnet/Open-XML-SDK/main/LICENSE) | FETCHED | ed03ba352313a4ba7019d5bed4bd3218ac17f3e44442a3bb1aaff54dcca9a2bc |
| PDFSHARP | [PDFSHARP](https://raw.githubusercontent.com/empira/PDFsharp/master/LICENSE) | FETCHED | 3c648a5072bd7f7386ca28687780489a708a57ed75f13927bc16dd3e34af3bf7 |
| PDFPIG | [PDFPIG](https://raw.githubusercontent.com/UglyToad/PdfPig/master/LICENSE) | FETCHED | 4c510e162f896ea43b4b1cf1b743641d7c756f1004d0e5eaf0615b28b7ded409 |
| INNO | [INNO](https://raw.githubusercontent.com/jrsoftware/issrc/main/license.txt) | FETCHED | 2e5346868c2a18434489824e11d65c3031620f792fefc415d05f19cd441abf5c |
| WIX | [WIX](https://raw.githubusercontent.com/wixtoolset/wix/main/LICENSE.TXT) | FETCHED | dfdf2048787635215a6baf3b9d461dee89a2904d246787258a44f072a98d4786 |
| TESSERACT | [TESSERACT](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/LICENSE) | FETCHED | cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30 |
| DOTNET_LICENSE | [DOTNET_LICENSE](https://raw.githubusercontent.com/dotnet/runtime/main/LICENSE.TXT) | FETCHED | cfc21f5e8bd655ae997eec916138b707b1d290b83272c02a95c9f821b8c87310 |
| NODE_LICENSE | [NODE_LICENSE](https://raw.githubusercontent.com/nodejs/node/main/LICENSE) | FETCHED | 3ebb7123f4d2b9b916338e11748380972d4339d66f54cb3258270f99bb62faf5 |
| ELECTRON_LICENSE | [ELECTRON_LICENSE](https://raw.githubusercontent.com/electron/electron/main/LICENSE) | FETCHED | 5154e165bd6c2cc0cfbcd8916498c7abab0497923bafcd5cb07673fe8480087d |
| TAURI_LICENSE | [TAURI_LICENSE](https://raw.githubusercontent.com/tauri-apps/tauri/dev/LICENSE_MIT) | UNAVAILABLE | HTTP Error 404: Not Found |
| RUST_LICENSE | [RUST_LICENSE](https://raw.githubusercontent.com/rust-lang/rust/master/LICENSE-APACHE) | FETCHED | 62c7a1e35f56406896d7aa7ca52d0cc0d272ac022b5d2796e7d6905db8a3636a |
| PLAYWRIGHT_SOURCE | [PLAYWRIGHT_SOURCE](https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/intro.md) | UNAVAILABLE | HTTP Error 404: Not Found |
| PYTHON_SOURCE | [PYTHON_SOURCE](https://raw.githubusercontent.com/python/cpython/3.13/Doc/using/windows.rst) | FETCHED | 9e2a25eec1bbcf5a0ca2a36fe727136be2a90aefd8a7fab7126eb75781e4b4a9 |
| PYTHON_LICENSE | [PYTHON_LICENSE](https://raw.githubusercontent.com/python/cpython/3.13/LICENSE) | FETCHED | 78b12c3a81360b357002334f0e70ea0e92eebf7a9b358805c03c48484945f3bb |
| SQLITE_SOURCE | [SQLITE_SOURCE](https://raw.githubusercontent.com/sqlite/sqlite/master/LICENSE.md) | FETCHED | c9053892d578840a196d588ff68baa9bc0f5240eb215fb9cf91cd6b0b3209305 |
| RUST_SOURCE | [RUST_SOURCE](https://raw.githubusercontent.com/rust-lang/rust/master/src/doc/rustc/src/platform-support/pc-windows-msvc.md) | UNAVAILABLE | HTTP Error 404: Not Found |
| TAURI_LICENSE_SOURCE | [TAURI_LICENSE_SOURCE](https://raw.githubusercontent.com/tauri-apps/tauri/dev/LICENSE-MIT) | FETCHED | 9dd42ea92cff2ede5cd477cbfcce051b2d0115c0ac7f368ee88cb545055dff1d |
| TAURI_SOURCE | [TAURI_SOURCE](https://raw.githubusercontent.com/tauri-apps/tauri/dev/crates/tauri/README.md) | FETCHED | d53737b76e569ea9d7af01d69be6fb729959b97bc08d0564a421c3917b584070 |
| QT_SOURCE | [QT_SOURCE](https://raw.githubusercontent.com/qt/qtbase/dev/LICENSES/LGPL-3.0-only.txt) | FETCHED | da7eabb7bafdf7d3ae5e9f223aa5bdc1eece45ac569dc21b3b037520b4464768 |
| ELECTRON_SOURCE | [ELECTRON_SOURCE](https://raw.githubusercontent.com/electron/electron/main/docs/tutorial/support.md) | FETCHED | 717946b6e7055a2fce56fa00f777ff889ff9fce556b2c4d8f45b8daebd21bfe4 |
| WEBVIEW_SOURCE | [WEBVIEW_SOURCE](https://raw.githubusercontent.com/MicrosoftDocs/edge-developer/main/microsoft-edge/webview2/concepts/supported-browsers.md) | UNAVAILABLE | HTTP Error 404: Not Found |
| INNO_SOURCE | [INNO_SOURCE](https://raw.githubusercontent.com/jrsoftware/issrc/main/README.md) | FETCHED | 584fd2dd2d3c8c308ec62e12321d271fd65ba0929951f2261b51236496cfc996 |
| QT_OS_SOURCE | [QT_OS_SOURCE](https://raw.githubusercontent.com/qt/qtdoc/dev/doc/src/platforms/supported-platforms.qdoc) | FETCHED | c11b0cdc17f0733c458f5c6360fdf47467d5147968304be96cdae12e157e35cc |
| DOTNET_POLICY | [DOTNET_POLICY](https://raw.githubusercontent.com/dotnet/core/main/release-policies.md) | FETCHED | 1ac8e94c454731cb540ad108183a3883749cb45c8e8a2fac0922c549d7284d0d |
| PLAYWRIGHT_INTRO | [PLAYWRIGHT_INTRO](https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/intro-js.md) | FETCHED | 4c932f4316b8791191e5a17404dae5c4b7dc1d38c0479883157264ddd91ff9ae |
| PLAYWRIGHT_DOTNET | [PLAYWRIGHT_DOTNET](https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/intro-csharp.md) | FETCHED | b1b68c46db8e9e79b6c72e5e6517de66e065bcf6f26f70757d160ab275acc36a |
| RUST_WIN | [RUST_WIN](https://raw.githubusercontent.com/rust-lang/rust/master/src/doc/rustc/src/platform-support/windows-msvc.md) | FETCHED | ab73771c02f7c349aacc2681ace9eec62821890b50262cf8bde6d25cf53fdd69 |
| WEBVIEW_OS | [WEBVIEW_OS](https://raw.githubusercontent.com/MicrosoftDocs/edge-developer/main/microsoft-edge/webview2/concepts/distribution.md) | FETCHED | ee253265cef0d6b52e407df5e24c9b2b0ea881f8ccb83d99dfd8722bce43ee56 |
| CHROMIUM_LICENSE | [CHROMIUM_LICENSE](https://raw.githubusercontent.com/chromium/chromium/main/LICENSE) | FETCHED | 368cca1106be99d39ecd32a38d8305585d802a475effb66380b91ffc9bcf709b |
| PYSIDE_SOURCE | [PYSIDE_SOURCE](https://raw.githubusercontent.com/pyside/pyside-setup/dev/LICENSES/LGPL-3.0-only.txt) | FETCHED | da7eabb7bafdf7d3ae5e9f223aa5bdc1eece45ac569dc21b3b037520b4464768 |
| QT_WINDOWS_SOURCE | [QT_WINDOWS_SOURCE](https://raw.githubusercontent.com/qt/qtdoc/dev/doc/src/platforms/windows.qdoc) | FETCHED | d886d394d8f3a373841e7a35a0b5613bd287b292f1d66743fa90a7ac5632746f |
| WEBVIEW_LICENSE | [WEBVIEW_LICENSE](https://raw.githubusercontent.com/MicrosoftEdge/WebView2Samples/main/LICENSE) | UNAVAILABLE | HTTP Error 404: Not Found |
