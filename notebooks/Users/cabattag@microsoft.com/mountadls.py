# Databricks notebook source
spark.conf.set("fs.azure.account.key.bikedatacabattag.dfs.core.windows.net", dbutils.secrets.get(scope = "bikedata", key = "storagekey"))
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "true")
dbutils.fs.ls("abfss://bike@bikedatacabattag.dfs.core.windows.net/")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "false")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "f989fd61-edef-44fc-9980-a3643b2eaa54",
           "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope = "bikedata", key = "oauthkey"),
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/token"}

# Optionally, you can add <your-directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bike@bikedatacabattag.dfs.core.windows.net/",
  mount_point = "/mnt/bike",
  extra_configs = configs)