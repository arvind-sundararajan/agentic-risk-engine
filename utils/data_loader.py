```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import Dict, List
from bedrock import StateGraph
from dspy import MemoryManagement

def load_non_stationary_drift_index(data: List[Dict]) -> List[float]:
    """
    Load non-stationary drift index from data.

    Args:
    - data (List[Dict]): List of dictionaries containing data.

    Returns:
    - List[float]: List of non-stationary drift indices.

    Raises:
    - Exception: If data is invalid.
    """
    try:
        logging.info('Loading non-stationary drift index...')
        non_stationary_drift_index = [item['drift_index'] for item in data]
        logging.info('Non-stationary drift index loaded.')
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error loading non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(data: List[Dict]) -> List[int]:
    """
    Perform stochastic regime switch on data.

    Args:
    - data (List[Dict]): List of dictionaries containing data.

    Returns:
    - List[int]: List of regime switch indices.

    Raises:
    - Exception: If data is invalid.
    """
    try:
        logging.info('Performing stochastic regime switch...')
        regime_switch_indices = [item['regime_switch'] for item in data]
        logging.info('Stochastic regime switch performed.')
        return regime_switch_indices
    except Exception as e:
        logging.error(f'Error performing stochastic regime switch: {e}')
        raise

def load_data(file_path: str) -> List[Dict]:
    """
    Load data from file.

    Args:
    - file_path (str): Path to file.

    Returns:
    - List[Dict]: List of dictionaries containing data.

    Raises:
    - Exception: If file is invalid.
    """
    try:
        logging.info(f'Loading data from {file_path}...')
        data = StateGraph.load(file_path)
        logging.info('Data loaded.')
        return data
    except Exception as e:
        logging.error(f'Error loading data: {e}')
        raise

def manage_memory(data: List[Dict]) -> None:
    """
    Manage memory for data.

    Args:
    - data (List[Dict]): List of dictionaries containing data.

    Raises:
    - Exception: If memory management fails.
    """
    try:
        logging.info('Managing memory...')
        MemoryManagement.optimize(data)
        logging.info('Memory managed.')
    except Exception as e:
        logging.error(f'Error managing memory: {e}')
        raise

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    data = [
        {'drift_index': 0.5, 'regime_switch': 1},
        {'drift_index': 0.7, 'regime_switch': 0},
        {'drift_index': 0.3, 'regime_switch': 1}
    ]
    non_stationary_drift_index = load_non_stationary_drift_index(data)
    regime_switch_indices = stochastic_regime_switch(data)
    print('Non-stationary drift index:', non_stationary_drift_index)
    print('Regime switch indices:', regime_switch_indices)
    manage_memory(data)
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```