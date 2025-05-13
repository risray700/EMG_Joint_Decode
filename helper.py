import torch
import pandas as pd


def compare_predictions(model, test_dataloader, angle_names=None):
    model.eval()
    all_data = {"ts": [], "channel": [], "actual": [], "predicted": []}
    import pdb
    pdb.set_trace()

    with torch.no_grad():
        for emg_inputs, joint_angles, info in test_dataloader:
            preds = model(emg_inputs)
            for i in range(joint_angles.shape[1]):
                all_data["actual"].extend(joint_angles[:, i].numpy())
                all_data["predicted"].extend(preds[:, i].numpy())
                all_data["channel"].extend(
                    [angle_names[i] if angle_names else f"angle_{i+1}"]
                    * len(joint_angles)
                )
                all_data["ts"].extend(info[:, 0].numpy())

    df = pd.DataFrame(all_data).sort_values(by=["channel", "ts"])
    return df
