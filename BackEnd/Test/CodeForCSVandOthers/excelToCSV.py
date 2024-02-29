from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'



# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = 'DropoutBihar.xlsx'  # file | Input file to perform the operation on.
output_encoding = 'output_encoding_example'  # str | Optional, set the output text encoding for the result; possible values are UTF-8, ASCII and UTF-32.  Default is UTF-8. (optional)

try:
    # Convert Excel XLSX Spreadsheet to CSV, Single Worksheet
    api_response = api_instance.convert_document_xlsx_to_csv(input_file, output_encoding=output_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_xlsx_to_csv: %s\n" % e)