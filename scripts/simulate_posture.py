import opensim as osim
import os

def load_model(model_path):
    model = osim.Model(model_path)
    model.setUseVisualizer(False)
    state = model.initSystem()
    print(f"Model loaded: {model.getName()}")
    return model, state

def set_standing_pose(model, state):
    coords = model.getCoordinateSet()

    for name in [
        "pelvis_tilt", "pelvis_list", "pelvis_rotation",
        "hip_flexion_r", "hip_flexion_l",
        "knee_angle_r", "knee_angle_l",
        "ankle_angle_r", "ankle_angle_l",
        "lumbar_extension", "lumbar_bending", "lumbar_rotation"
    ]:
        if coords.contains(name):
            coords.get(name).setValue(state, 0.0)

    print("Neutral standing posture set.")
    return state

def run_forward_simulation(model, state, duration=0.05):
    model.equilibrateMuscles(state)
    model.realizeVelocity(state)
    state.setTime(0)

    print("Running simulation...")
    manager = osim.Manager(model)
    manager.setIntegratorAccuracy(1e-2)
    manager.initialize(state)

    print("Starting integration...")
    manager.integrate(duration)

    # Save the result
    output_dir = os.path.join("..", "data", "outputs")
    os.makedirs(output_dir, exist_ok=True)

    storage = manager.getStateStorage()
    output_basename = "standing_simulation"
    output_dt = 0.0  # Use 0.0 to auto-sample or choose another step

    print(f"Saving to: {os.path.join(output_dir, output_basename + '.sto')}")
    osim.Storage.printResult(storage, output_basename, output_dir, output_dt, ".sto")

    print(f"✔ Simulation output saved in: {output_dir}")

def main():
    model_path = os.path.join("..", "models", "MaleFullBodyModel_v2.0_OS4.osim")
    model, state = load_model(model_path)
    state = set_standing_pose(model, state)

    # Save model snapshot
    model.printToXML(os.path.join("..", "models", "NeutralStanding.osim"))

    run_forward_simulation(model, state)

if __name__ == "__main__":
    main()
