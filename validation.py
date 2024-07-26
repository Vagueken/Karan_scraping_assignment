class Validation:
    def __init__(self, product_data):
        self.product_data = product_data
        self.errors = []

    def validate(self):
        self.validate_mandatory_fields()
        self.validate_prices()
        self.validate_variants()
        self.validate_images()
        self.validate_categories()
        # Add more validation rules as needed
        return self.errors

    def validate_mandatory_fields(self):
            # Check if at least one of title or name is present
            if not any(self.product_data.get(field) for field in ['title', 'name']):
                self.errors.append("Missing mandatory field: one of 'title' or 'name' must be present")
            
            # Check if model_id is present
            if 'model_id' not in self.product_data or not self.product_data['model_id']:
                self.errors.append("Missing mandatory field: 'model_id'")
            
            # Check if at least one of id, product_id, or sku is present
            if not any(self.product_data.get(field) for field in ['id', 'product_id', 'sku']):
                self.errors.append("Missing mandatory field: one of 'id', 'product_id', or 'sku' must be present")
    def validate_prices(self):
        original_price = self.product_data.get('original_price')
        sale_price = self.product_data.get('sale_price')
        if original_price is not None and sale_price is not None:
            if sale_price > original_price:
                self.errors.append("Sale price is greater than original price")

    def validate_variants(self):
        if 'variants' in self.product_data:
            for variant in self.product_data['variants']:
                if 'images' not in variant or not variant['images']:
                    self.errors.append(f"Variant {variant.get('id', 'sku')} has no images")
                if 'price' not in variant or not variant['price']:
                    self.errors.append(f"Variant {variant.get('id', 'sku')} has no price")

    def validate_images(self):
        if 'images' not in self.product_data or not self.product_data['images']:
            self.errors.append("No images found for the product")

    def validate_categories(self):
        if 'options' in self.product_data:
            if not isinstance(self.product_data['options'], list) or not self.product_data['options']:
                self.errors.append("Categories must be a non-empty list")
        else:
            self.errors.append("Missing categories field")


if __name__ == "__main__":
    # This should be replaced with actual scraped data
    sample_product_data = {
        'title': 'Sample Product',
        'product_id': '12345',
        'model_id': '67890',
        'original_price': 100.00,
        'sale_price': 80.00,
        'variants': [
            {
                'model_id': 'var1',
                'price': 75.00,
                'images': ['image1.jpg']
            }
        ],
        'images': ['image1.jpg', 'image2.jpg'],
        'options': ['option1', 'option2']
    }

    validator = Validation(sample_product_data)
    validation_errors = validator.validate()

    if validation_errors:
        print("Validation errors found:")
        for error in validation_errors:
            print(f" - {error}")
    else:
        print("All validations passed!")
