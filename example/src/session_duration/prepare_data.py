import argparse

import pandas as pd
from sklearn.model_selection import train_test_split

from session_duration.config import ensure_parent, load_params


def split_dataset(
    data: pd.DataFrame,
    test_size: float,
    random_state: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split the dataset while preserving the target column."""
    return train_test_split(data, test_size=test_size, random_state=random_state)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()

    params = load_params(args.params)
    data = pd.read_csv(params["data"]["raw_path"])

    train_data, test_data = split_dataset(
        data=data,
        test_size=float(params["split"]["test_size"]),
        random_state=int(params["split"]["random_state"]),
    )

    train_path = ensure_parent(params["data"]["processed_train_path"])
    test_path = ensure_parent(params["data"]["processed_test_path"])
    train_data.to_csv(train_path, index=False)
    test_data.to_csv(test_path, index=False)
    print(f"Train guardado en {train_path} ({len(train_data)} filas).")
    print(f"Test guardado en {test_path} ({len(test_data)} filas).")


if __name__ == "__main__":
    main()

