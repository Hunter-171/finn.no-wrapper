# finn.no-wrapper
Simple wrapper for scraping page data from the norwegian marketplace [finn.no](https://finn.no)

### EXAMPLE USAGE
**main.py**
```python
from page import Page

page = Page(275680888)

print("Page Information: ")
print(f"""
Title: {page.title}
Price: {page.price} NOK
Description: {page.description}
Sold: {page.sold}

City: {page.location["postalPlace"]}
Categories: {page.categories}
""")
```

**OUTPUT**
```
Page Information: 

Title: Msi GTX 970
Price: 400 NOK
Description: Selger mitt gamle msi skjermkort grunnet opgradering i fjor.

Skjermkortet ble brukt til hovedsakelig gaming og kan fint kjøre de populære spillene.

Pris kan diskuteres
Sold: True

City: Kristiansand S
Categories: ['Elektronikk og hvitevarer', 'Data', 'Stasjonær PC']
```

### EXAMPLE JSON DATA
accessible through `page.full_data`
```json
{
  "adId": 301565566,
  "brand": "FINN",
  "userOwner": true,
  "objectUserId": "1297297582",
  "isPreview": false,
  "url": {
    "baseUrl": "https://www.finn.no",
    "favoriteBaseURL": "/favorittliste/podium-resource/favorittlistePodlet/favorite-api",
    "trackJsURL": "https://assets.finn.no/pkg/@finn-no/track-js-loader/v3/autoloader.js",
    "broadcastURL": "/broadcasts"
  },
  "locale": "nb-NO",
  "kind": "BAP",
  "unleashToggles": {
    "newMapEnabled": true
  },
  "objectData": {
    "ad": {
      "price": 1200,
      "title": "Nvidia 1070 Founders Edition",
      "extras": [
        {
          "id": "computeracc_type",
          "label": "Type",
          "value": "Komponenter"
        },
        {
          "id": "condition",
          "label": "Tilstand",
          "value": "Brukt"
        }
      ],
      "images": [
        {
          "uri": "https://images.finncdn.no/dynamic/default/2023/5/vertical-0/02/6/301/565/566_2127084706.jpg",
          "width": 1600,
          "height": 1208
        },
        {
          "uri": "https://images.finncdn.no/dynamic/default/2023/5/vertical-0/02/6/301/565/566_843094196.jpg",
          "width": 1600,
          "height": 1330
        },
        {
          "uri": "https://images.finncdn.no/dynamic/default/2023/5/vertical-0/02/6/301/565/566_1437053508.jpg",
          "width": 1600,
          "height": 954
        },
        {
          "uri": "https://images.finncdn.no/dynamic/default/2023/5/vertical-0/02/6/301/565/566_1595549240.jpg",
          "width": 1600,
          "height": 1368
        }
      ],
      "category": [
        "Elektronikk og hvitevarer",
        "Data",
        "Datatilbeh�r"
      ],
      "dealerAd": false,
      "location": {
        "position": {
          "lat": 62.45553924996945,
          "lng": 6.360253117631279,
          "links": {
            "norortho": {
              "uri": "https://kart.finn.no?finnkode=301565566&lat=62.45553924996945&lng=6.360253117631279&mapType=norortho&showPin=0&bl=1",
              "title": "Flyfoto"
            },
            "finnhybrid": {
              "uri": "https://kart.finn.no?finnkode=301565566&lat=62.45553924996945&lng=6.360253117631279&mapType=finnhybrid&showPin=0&bl=1",
              "title": "Hybridkart"
            },
            "finnvector": {
              "uri": "https://kart.finn.no?finnkode=301565566&lat=62.45553924996945&lng=6.360253117631279&mapType=finnvector&showPin=0&bl=1",
              "title": "Stort kart"
            }
          },
          "accuracy": 5,
          "mapImage": "https://maptiles.finncdn.no/staticmap?lat=62.45553924996945&lng=6.360253117631279&zoom=12&size=400x300&maptype=norwayVector&showPin=false"
        },
        "postalCode": "6010",
        "countryName": "Norge",
        "postalPlace": "�lesund"
      },
      "adViewType": "bap-sell",
      "description": "Selger brukt Nvidia 1070 founders edition skjermkort.",
      "adViewTypeLabel": "Til salgs"
    },
    "meta": {
      "adId": 301565566,
      "mode": "PLAY",
      "edited": "2023-05-02T18:43:59.694523+02:00",
      "history": [
        {
          "mode": "PLAY",
          "version": "15.1",
          "broadcasted": "2023-05-02T18:44:37.599240656+02:00"
        }
      ],
      "ownerId": 1297297582,
      "version": "15.1",
      "occurred": "2023-05-02T18:44:37.599240656+02:00",
      "ownerUrn": "sdrn:finn:user:1297297582",
      "schemaName": "bap-sell",
      "schemaVersion": "1.3.0"
    }
  },
  "initialImage": 0,
  "beenPublished": true,
  "trustObjectProfile": {
    "redirect": null,
    "content": "\n        <div\n            id=\"trust-object-profile-podlet\"\n            data-mount-origin=\"https://www.finn.no\"\n            data-public-pathname=\"/bap/api/podium-resource/trustObjectProfilePodlet\"\n        ><div class=\"bg-white p-16 rounded-8 border border-bluegray-200\" data-reactroot=\"\"><h2 class=\"hidden\">Profilinfo</h2><div class=\"flex gap-8 items-center\"><svg class=\"w-64 h-64 rounded-full block shrink-0\" viewBox=\"0 0 56 56\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\" aria-label=\"Generisk profilbilde\"><circle cx=\"28\" cy=\"28\" r=\"27\" fill=\"#F1F5F9\"></circle><path d=\"M17.142 16.202A20.907 20.907 0 0 0 32.2 22.6a20.94 20.94 0 0 0 8.28-1.704m4.111 28.406a23.39 23.39 0 0 0-33.182 0M40.6 22.6c0 6.959-5.641 12.6-12.6 12.6s-12.6-5.641-12.6-12.6S21.041 10 28 10s12.6 5.641 12.6 12.6ZM55 28c0 14.912-12.088 27-27 27S1 42.912 1 28 13.088 1 28 1s27 12.088 27 27Z\" stroke=\"#C3CCD9\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path></svg><p class=\"m-0\">Du m� v�re logget inn for � se profilen og sende melding</p></div><a href=\"/auth/login\" class=\"mt-16 max-w-full w-full button      button--small    \">Logg inn</a></div></div>\n\n        <script id=\"trust-object-profile-podlet-data\" type=\"application/json\">\n            {\"loggedIn\":false}\n        </script>\n        ",
    "headers": {
      "podlet-version": "20230530112438-91a388a",
      "content-type": "text/html; charset=utf-8",
      "content-length": "1288",
      "etag": "W/\"508-SzKANnZv+cO5j2K+0umAYR+ggfk\"",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [
      {
        "value": "https://assets.finn.no/pkg/trust-object-profile-podlet/1.0.80/styles.css",
        "type": "text/css",
        "rel": "stylesheet"
      }
    ],
    "js": [
      {
        "value": "https://assets.finn.no/pkg/trust-object-profile-podlet/1.0.80/index.js",
        "type": "module"
      }
    ]
  },
  "contactButton": {
    "redirect": null,
    "content": "\n        <script id=\"contact-button-data\" type=\"application/json\">\n            {\"name\":\"contact-button-podlet\",\"url\":\"/auth/login?redirectUrl=https%3A%2F%2Ffinn.no%2F301565566\",\"isAdOwner\":false,\"adId\":\"301565566\",\"requireEid\":false,\"preview\":\"false\",\"locale\":\"nb\",\"brand\":\"FINN\"}\n        </script>\n        \n    ",
    "headers": {
      "podlet-version": "20230620123950-43b0e78",
      "content-type": "text/html; charset=utf-8",
      "content-length": "312",
      "etag": "W/\"138-DWjjf2+WlOXCtPFN1oz3Y/taMG0\"",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [],
    "js": [
      {
        "value": "https://assets.finn.no/pkg/contact-button-podlet/1.0.59/index.js",
        "type": "module"
      }
    ]
  },
  "offerButton": {
    "redirect": null,
    "content": "<create-offer-button>\n                <link href=https://assets.finn.no/pkg/tjt-podlet-create-offer-button/1.0.124/styles.css media=\"all\" type=\"text/css\" rel=\"stylesheet\" />\n                <div id=\"tjt-podlet-create-offer-button\" data-props=eyJmaW5ua29kZSI6IjMwMTU2NTU2NiIsInN0eWxlbGluayI6Imh0dHBzOi8vYXNzZXRzLmZpbm4ubm8vcGtnL3RqdC1wb2RsZXQtY3JlYXRlLW9mZmVyLWJ1dHRvbi8xLjAuMTI0L3N0eWxlcy5jc3MiLCJ1aVRleHQiOnsic2VjdGlvbnMiOnsic2lkZWJhciI6eyJvcHRlZEluIjp7InRyYWRlVHlwZVRleHQiOiJUaWwgc2FsZ3MiLCJwcmljZVRleHQiOiIxwqAyMDAga3IiLCJzaGlwcGluZ1ByaWNlIjp7InRleHQiOiJGcmFrdCBmcmEgMzkga3IgKyBUcnlnZyBiZXRhbGluZyJ9LCJwYXltZW50VGV4dCI6IkJldGFsIG1lZCBrb3J0IGVsbGVyIiwiYWN0aW9ucyI6eyJpbml0VHJhbnNhY3Rpb24iOnsidGV4dCI6Iktqw7hwIG1lZCBGaWtzIGZlcmRpZyIsImRpc2FibGVkIjpmYWxzZX19LCJjYWxsb3V0IjoiRmlrcyBmZXJkaWciLCJzZXJ2aWNlSW5mbyI6eyJ0aXRsZSI6IkZpa3MgZmVyZGlnIiwidGV4dCI6IkVua2VsIGJldGFsaW5nIG9nIGZyYWt0IGdqZW5ub20gRklOTiIsImRldGFpbHMiOlt7InRpdGxlIjoiR2kgYnVkIG9nIGJldGFsIG1lZCBWaXBwcyBlbGxlciBrb3J0In0seyJ0aXRsZSI6IlZhcmVuIHNlbmRlcyB0aWwgZGVnIn0seyJ0aXRsZSI6IkR1IGhhciAyNCB0aW1lciB0aWwgw6Ugc2pla2tlIHZhcmVuIn1dLCJhY3Rpb25zIjp7Im1vcmVJbmZvIjp7InRleHQiOiJMZXMgbWVyIG9tIEZpa3MgZmVyZGlnIiwiZGlzYWJsZWQiOmZhbHNlLCJsaW5rIjoiaHR0cHM6Ly93d3cuZmlubi5uby9iYXAvYXJ0aWtsZXIvYWt0dWVsdC9maWtzLWZlcmRpZyJ9fX0sInNoaXBwaW5nSW5mbyI6eyJ0aXRsZSI6IlZhcmVuIGthbiBzZW5kZXMgbWVkIiwiaGVsdGhqZW0iOnsidGl0bGUiOiJIZWx0aGplbSIsInRleHQiOiJEdSBiZXRhbGVyIDM5IGtyIGZvciBmcmFrdGVuIn0sInBvc3RlbiI6eyJ0aXRsZSI6IlBvc3RlbiIsInRleHQiOiJEdSBiZXRhbGVyIDM5IGtyIGZvciBmcmFrdGVuIn0sInByb3ZpZGVycyI6W3sidGl0bGUiOiJIZWx0aGplbSIsInRleHQiOiJEdSBiZXRhbGVyIDM5IGtyIGZvciBmcmFrdGVuIiwibmFtZSI6IkhFTFRISkVNIn0seyJ0aXRsZSI6IlBvc3RlbiIsInRleHQiOiJEdSBiZXRhbGVyIDM5IGtyIGZvciBmcmFrdGVuIiwibmFtZSI6IlBPU1RFTiJ9XX0sInNhZmVQYXltZW50SW5mbyI6eyJ0aXRsZSI6IlRyeWdnIGJldGFsaW5nIiwiZGV0YWlscyI6W3sidGl0bGUiOiJEdSBiZXRhbGVyIGbDuHIgdmFyZW4gc2VuZGVzIn0seyJ0aXRsZSI6IkZJTk4gcGFzc2VyIHDDpSBwZW5nZW5lIHRpbCBkdSBoYXIgZsOldHQgdmFyZW4ifSx7InRpdGxlIjoiRHUgZsOlciAyNCB0aW1lciB0aWwgw6Ugc2UgYXQgYWx0IGVyIGkgb3JkZW4gZsO4ciB2aSB1dGJldGFsZXIgcGVuZ2VuZSJ9XX19LCJjb250YWN0U2VsbGVyIjp7InRleHQiOiJIdmlzIGR1IGx1cmVyIHDDpSBub2Ugb20gdmFyZW4sIHPDpSBzZW5kIGVuIG1lbGRpbmcgdGlsIHNlbGdlciIsImFjdGlvbnMiOnsiY29udGFjdFNlbGxlciI6eyJ0ZXh0IjoiS29udGFrdCBzZWxnZXIiLCJkaXNhYmxlZCI6ZmFsc2V9fX19fX0sImlzT3duQWQiOmZhbHNlLCJhcGlFbmRwb2ludCI6Ii9iYXAvYXBpL3BvZGl1bS1yZXNvdXJjZS9jcmVhdGVPZmZlckJ1dHRvblBvZGxldCIsImlzUHJldmlld01vZGUiOmZhbHNlfQ==><section class=\"md:border border-bluegray-200 relative rounded-8\" aria-label=\"Kj�p varen\"><div class=\"absolute text-14 font-bold text-yellow-900 bg-yellow-100 right-0 top-0 px-12 py-8 rounded-bl-8 rounded-tr-8 hidden md:block\">Fiks ferdig</div><div class=\"pb-32 md:p-24\"><h2 class=\" text-16 md:text-12 text-gray-700 md:text-gray-500 mb-0 mt-8\">Til salgs</h2><div class=\"mb-4 md:mb-24 mt-4\"><div class=\"h2\">1�200 kr</div><p class=\"flex-grow self-end text-14 mb-12\" aria-hidden=\"false\">Frakt fra 39 kr + Trygg betaling</p></div><div class=\"flex flex-col-reverse md:flex-col\"><div><button class=\"w-full max-w-full button button--primary         \" type=\"button\">Kj�p med Fiks ferdig</button></div></div><button class=\"pt-12 font-bold hover:no-underline text-14 button        button--link  \" type=\"button\">Les mer om Fiks ferdig</button></div></section></div>\n            </create-offer-button>",
    "headers": {
      "podlet-version": "20230617080141-dfc3ba1a",
      "content-type": "text/html; charset=utf-8",
      "content-length": "3311",
      "etag": "W/\"cef-BJjiGqCqZgcD18h7YI8p8gm2VGI\"",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [],
    "js": [
      {
        "value": "https://assets.finn.no/pkg/tjt-podlet-create-offer-button/1.0.124/index.js",
        "type": "module"
      }
    ]
  },
  "adShippable": null,
  "dataMltPodlet": {
    "redirect": null,
    "content": "\n                    <data-podlet-mlt initial-state='{\"title\":\"Andre ting p� Torget\",\"baseUrl\":\"/bap/api/podium-resource/dataPodletMltPodlet/match-ad\",\"deviceType\":\"desktop\",\"imagesCdnUrl\":\"https://images.finncdn.no\",\"favoritesListUrl\":\"https://www.finn.no/favorittliste/podium-resource/favorittlistePodlet/favorite-api\",\"product\":\"bap\",\"rows\":\"6\",\"pages\":\"8\",\"position\":\"bap-object_v2ads\",\"adId\":\"301565566\",\"headingLevel\":2,\"fallbackTitle\":\"\",\"fallbackProduct\":\"\",\"fallbackType\":\"\",\"resourceMountPath\":\"/bap/api/podium-resource/dataPodletMltPodlet\",\"type\":\"mlt\",\"url\":\"https://www.finn.no/bap/api/podium-resource/dataPodletMltPodlet\",\"consentClient\":\"WEB_DESKTOP\",\"showOverflowMenu\":false,\"useFabric\":false,\"useBannerAd\":false,\"previewType\":\"finncode\",\"previewId\":\"\",\"suppressTitle\":false,\"css\":\"https://assets.finn.no/pkg/data-podlet-server/1.0.181/style.css\",\"disableBlinkScript\":\"true\"}'>\n                    </data-podlet-mlt>\n                ",
    "headers": {
      "podlet-version": "b0da5273f",
      "content-type": "text/html; charset=utf-8",
      "content-length": "950",
      "etag": "W/\"3b6-0ofktPgSAA2IJX8QVndnO3Cz8rE\"",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [],
    "js": [
      {
        "value": "https://assets.finn.no/pkg/data-podlet-server/1.0.181/scripts.js",
        "type": "module"
      }
    ]
  },
  "pfTipsCallout": {
    "redirect": null,
    "content": "",
    "headers": {
      "podlet-version": "20221117181529-369e5d8",
      "content-type": "text/plain; charset=utf-8",
      "x-response-time": "10.127609252929688",
      "content-length": "0",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [],
    "js": []
  },
  "pfFinanceLinks": {
    "redirect": null,
    "content": "\n        <bfft-links finncode=\"301565566\"  ssr>\n          <template><div class=\"mx-16 mt-16\">\n\n  \n  </div></template>\n        </bfft-links>\n      ",
    "headers": {
      "podlet-version": "bba6abf-1686053391",
      "content-type": "text/html; charset=utf-8",
      "x-response-time": "9.956140518188477",
      "content-length": "146",
      "date": "Tue, 27 Jun 2023 19:35:03 GMT",
      "connection": "keep-alive",
      "keep-alive": "timeout=5"
    },
    "css": [],
    "js": [
      {
        "value": "https://assets.finn.no/pkg/pf-bfft-links/0.9.29/pf-bfft-links.js",
        "type": "module"
      }
    ]
  },
  "shouldLoadHotjar": false
}
```
