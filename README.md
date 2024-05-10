# Operationalizing Machine Learning

The goal of this project is to use AzureML to configure a cloud-based machine learning production model, then deploy it to an endpoint for consumtion. Furthermore, the whole workflow will be built into a automated pipeline, which will then be published and consumed whenever we need to retrain the model.
The [Bank Marketing dataset](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) is used as the training dataset for the AutoML model.

## Architectural Diagram
![Architectural Diagram of the project](Architectural Diagram.png)

## Key Steps
### 1. Create and run Auto ML Experiment
In this step, an experiment using Automated ML is created and run using a compute cluster.
![Bankmarketing Dataset is registered in Datasets](./screenshots/step2_registered_dataset.png)

![Experiment run is completed](./screenshots/step2_experiment_completed.png)

![The best model is selected](./screenshots/step2_best_model.png)

### 2. Deploy the model
In this step, we deploy the best model in step 1.
(no screenshots are required)
### 3. Enable Application Insights
In this step, we enable Application Insights and retrieve logs.

![Application Insights Enabled](./screenshots/step4_appinsights_enabled.png)

![Displayed the logs](./screenshots/step4_logs.png)

### 4. Consume model using Swagger

In this step, we consume the deployed model using Swagger.

![Swagger Documentation Overview](./screenshots/step5_swagger_api.png)

![Swagger Documentation for POST request](./screenshots/step5_swagger_api_post.png)

### 5. Consume Model Endpoints
In this step, we run the endpoint.py script to interact with the deployed model endpoint.

![Request the endpoint and get output](./screenshots/step6_run_endpoint.png)

### 6. Create, Publish and Consume a Pipeline

In this step, we use the [Jupyter Notebook](./aml-pipelines-with-aml-step.ipynb) to create and publish the Pipeline.

![Pipeline created](./screenshots/step7_pipeline_created.png)

![Pipeline details](./screenshots/step7_pipeline_details.png)

![Pipeline endpoint](./screenshots/step7_pipeline_endpoint.png)

![Published Pipeline](./screenshots/step7_pipeline_published.png)

![Pipeline Steps](./screenshots/step7_pipeline_steps_run.png)

![Scheduled Pipeline Run](./screenshots/step7_pipeline_scheduled_run.png)

## Screen Recording
This screencast [YouTube video](https://www.youtube.com/watch?v=BbxIHmh-Qw0) demonstrates the entire process of the working ML application:
- Working deployed ML model endpoint
- Deployed pipeline
- Available AutoML model
- Successful API requests to the endpoint with a JSON payload

## Future Work

To further improving the project, some suggestions are:
- Handling the data imbalance issue
- Experiment with longer AutoML run timeout to search for better models
- Enhance the data collection step in the pipeline to automate data collection and versioning.