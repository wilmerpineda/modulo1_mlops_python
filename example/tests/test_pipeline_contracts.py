from session_duration.generate_data import build_mock_sessions
from session_duration.train import CATEGORICAL_FEATURES, NUMERIC_FEATURES, TARGET_COLUMN, evaluate


def test_mock_dataset_has_expected_columns() -> None:
    data = build_mock_sessions(n_samples=50, random_state=42, noise_std=3.0)
    expected_columns = set(NUMERIC_FEATURES + CATEGORICAL_FEATURES + [TARGET_COLUMN])

    assert expected_columns.issubset(data.columns)
    assert len(data) == 50
    assert data[TARGET_COLUMN].min() > 0


def test_regression_metrics_contract() -> None:
    metrics = evaluate([10.0, 20.0, 30.0], [12.0, 18.0, 33.0])

    assert set(metrics) == {"mae", "rmse", "r2"}
    assert all(isinstance(value, float) for value in metrics.values())

