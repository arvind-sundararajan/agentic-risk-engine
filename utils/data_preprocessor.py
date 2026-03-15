```json
{
    "utils/data_preprocessor.py": {
        "content": "
import logging
from typing import List, Dict
from bedrock import StateGraph
from dspy import MemoryManager

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.

    Raises:
    - ValueError: If the input dataset is empty.
    """
    try:
        if not data:
            raise ValueError('Input dataset is empty')
        logging.info('Calculating non-stationary drift index')
        return sum(data) / len(data)
    except Exception as e:
        logging.error(f'Error calculating non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(data: List[float], threshold: float) -> bool:
    """
    Determine if a stochastic regime switch has occurred based on the given dataset and threshold.

    Args:
    - data (List[float]): The input dataset.
    - threshold (float): The threshold value.

    Returns:
    - bool: True if a stochastic regime switch has occurred, False otherwise.

    Raises:
    - ValueError: If the input dataset is empty or the threshold is invalid.
    """
    try:
        if not data or threshold < 0:
            raise ValueError('Invalid input dataset or threshold')
        logging.info('Checking for stochastic regime switch')
        return non_stationary_drift_index(data) > threshold
    except Exception as e:
        logging.error(f'Error checking for stochastic regime switch: {e}')
        raise

def memory_management(data: Dict[str, float]) -> None:
    """
    Manage memory usage for the given dataset.

    Args:
    - data (Dict[str, float]): The input dataset.

    Raises:
    - ValueError: If the input dataset is empty.
    """
    try:
        if not data:
            raise ValueError('Input dataset is empty')
        logging.info('Managing memory usage')
        MemoryManager().manage_memory(data)
    except Exception as e:
        logging.error(f'Error managing memory usage: {e}')
        raise

def state_graph_update(state_graph: StateGraph, data: List[float]) -> None:
    """
    Update the state graph with the given dataset.

    Args:
    - state_graph (StateGraph): The state graph to update.
    - data (List[float]): The input dataset.

    Raises:
    - ValueError: If the input dataset is empty.
    """
    try:
        if not data:
            raise ValueError('Input dataset is empty')
        logging.info('Updating state graph')
        state_graph.update(data)
    except Exception as e:
        logging.error(f'Error updating state graph: {e}')
        raise

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold = 3.0
    state_graph = StateGraph()
    memory_data = {'key1': 1.0, 'key2': 2.0}

    non_stationary_drift_index(data)
    stochastic_regime_switch(data, threshold)
    memory_management(memory_data)
    state_graph_update(state_graph, data)
",
        "commit_message": "feat: implement specialized data_preprocessor logic"
    }
}
```