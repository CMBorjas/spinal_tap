import opensim as osim

def load_model(model_path):
    """
    Load an OpenSim model from the specified path.
    
    Parameters:
    model_path (str): Path to the OpenSim model file (.osim).
    
    Returns:
    osim.Model: Loaded OpenSim model.
    """
    model = osim.Model(model_path)
    model.initSystem()
    print(f"Model loaded successfully{model.getname()}.")
    return model


def main():
    model_path = "../models/MaleFullBodyModel_v2.0_OS4.osim"  # Replace with your model path
    model = load_model(model_path)