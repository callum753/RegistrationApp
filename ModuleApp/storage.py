from storages.backends.azure_storage import AzureStorage
class AzureMediaStorage(AzureStorage):
    account_name = 'c0013851dcbs'
    account_key = '2zXe370Ddx/XMWP4M1f2XMYBs33kaqqS+E9+yMQGevqGNN8rzHbZZ3RFcwj8NS91440VNUmoqJ97+AStGAUWbA=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
	account_name = 'c0013851dcbs'
	account_key = '2zXe370Ddx/XMWP4M1f2XMYBs33kaqqS+E9+yMQGevqGNN8rzHbZZ3RFcwj8NS91440VNUmoqJ97+AStGAUWbA=='
	azure_container = 'static'
	expiration_secs = None
