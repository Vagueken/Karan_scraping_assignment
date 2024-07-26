import requests
import json
from validation import Validation

def validate_data(data):
    validator = Validation(data)
    errors = validator.validate()
    if errors:
        print("Validation errors found:")
        for error in errors:
            print(f" - {error}")
    else:
        print("All validations passed!")

query_payload = {
    "operationName": "SearchProduct",
    "variables": {
        "storeCode": "TJ",
        "published": "1",
        "sku": "077513"
    },
    "query": """
    query SearchProduct($sku: String, $storeCode: String = "TJ", $published: String = "1") {
      products(
        filter: {sku: {eq: $sku}, store_code: {eq: $storeCode}, published: {eq: $published}}
      ) {
        items {
          category_hierarchy {
            id
            url_key
            description
            name
            position
            level
            created_at
            updated_at
            product_count
            __typename
          }
          item_story_marketing
          product_label
          fun_tags
          primary_image
          primary_image_meta {
            url
            metadata
            __typename
          }
          other_images
          other_images_meta {
            url
            metadata
            __typename
          }
          context_image
          context_image_meta {
            url
            metadata
            __typename
          }
          published
          sku
          url_key
          name
          item_description
          item_title
          item_characteristics
          item_story_qil
          use_and_demo
          sales_size
          sales_uom_code
          sales_uom_description
          country_of_origin
          availability
          new_product
          promotion
          price_range {
            minimum_price {
              final_price {
                currency
                value
                __typename
              }
              __typename
            }
            __typename
          }
          retail_price
          nutrition {
            display_sequence
            panel_id
            panel_title
            serving_size
            calories_per_serving
            servings_per_container
            details {
              display_seq
              nutritional_item
              amount
              percent_dv
              __typename
            }
            __typename
          }
          ingredients {
            display_sequence
            ingredient
            __typename
          }
          allergens {
            display_sequence
            ingredient
            __typename
          }
          created_at
          first_published_date
          last_published_date
          updated_at
          related_products {
            sku
            item_title
            primary_image
            primary_image_meta {
              url
              metadata
              __typename
            }
            price_range {
              minimum_price {
                final_price {
                  currency
                  value
                  __typename
                }
                __typename
              }
              __typename
            }
            retail_price
            sales_size
            sales_uom_description
            category_hierarchy {
              id
              name
              __typename
            }
            __typename
          }
          __typename
        }
        total_count
        page_info {
          current_page
          page_size
          total_pages
          __typename
        }
        __typename
      }
    }
    """
}

# Set up the URL and headers
url = "https://www.traderjoes.com/api/graphql"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Content-Type": "application/json",
    "Cookie": "AMCVS_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=1; gpv_c51=https%3A%2F%2Fwww.traderjoes.com%2Fhome%2Fproducts%2Fpdp%2Forganic-mango-vinaigrette-dressing-077513; s_vncm=1722450599341%26vn%3D1; s_ivc=true; s_lv_s=First%20Visit; s_visit=1; s_dur=1721911249352; s_inv=0; s_cc=true; AMCV_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=-2121179033%7CMCIDTS%7C19930%7CMCMID%7C60936142052000780084376560919987732561%7CMCAAMLH-1722516049%7C12%7CMCAAMB-1722516049%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721918449s%7CNONE%7CMCSYNCSOP%7C411-19937%7CvVersion%7C5.3.0; _gid=GA1.2.302501694.1721911250; s_ptc=%5B%5BB%5D%5D; affinity=\"d8da0e84ae064784\"; _gat_UA-15671700-1=1; _ga_2HMPBJHQ41=GS1.1.1721911249.1.1.1721911881.0.0.0; _ga=GA1.1.1310015883.1721911250; s_plt=1.06; s_pltp=www.traderjoes.com%7Chome%7Cproducts%7Cpdp%7Corganic-mango-vinaigrette-dressing-077513; s_nr30=1721911882136-New; s_lv=1721911882136; s_ips=347; s_tp=347; s_ppv=www.traderjoes.com%257Chome%257Cproducts%257Cpdp%257Corganic-mango-vinaigrette-dressing-077513%2C100%2C100%2C347%2C1%2C1; s_tslv=1721911882139; s_pvs=%5B%5BB%5D%5D; s_tps=%5B%5BB%5D%5D",
    "Origin": "https://www.traderjoes.com",
    "Priority": "u=1, i",
    "Referer": "https://www.traderjoes.com/home/products/pdp/organic-mango-vinaigrette-dressing-077513",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# Make the POST request
response = requests.post(url, json=query_payload, headers=headers)


if response.status_code == 200:
    response_json = response.json()
    with open('traderjoes.json', 'w') as file:
        json.dump(response_json, file, indent=4)
    print("Response saved to traderjoes.json")
    
    print("Response JSON:")
    print(json.dumps(response_json, indent=4))
    
    if isinstance(response_json, dict) and 'data' in response_json:
        data = response_json['data']
        if 'products' in data and 'items' in data['products']:
            products = data['products']['items']
            if isinstance(products, list):
                for product in products:
                    print(f"Validating product data: {product}")
                    validate_data(product)
            else:
                print("Error: 'items' key does not contain a list")
        else:
            print("Error: 'products' key or 'items' key is missing in 'data'")
    else:
        print("Error: Response JSON does not contain 'data' key or is not a dictionary")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)