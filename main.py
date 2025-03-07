from src.pipeline import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline(config_path="script_config.yaml")
    pipeline.run()