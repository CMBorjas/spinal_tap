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
    output_path = os.path.join("..", "data", "outputs", "standing_simulation.sto")
    print(f"Saving to: {output_path}")
    manager.getStateStorage().print(output_path)
    print(f"✔ Simulation output saved at {output_path}")

def main():
    model_path = os.path.join("..", "models", "MaleFullBodyModel_v2.0_OS4.osim")
    model, state = load_model(model_path)
    state = set_standing_pose(model, state)

    # Save model snapshot
    model.printToXML(os.path.join("..", "models", "NeutralStanding.osim"))

    # ✅ Make sure this line is NOT missing
    run_forward_simulation(model, state)

if __name__ == "__main__":
    main()
