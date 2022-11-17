# Copyright 2022 The jax_triton Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for pallas-core functionality."""
import contextlib
import dataclasses

from typing import Any, Iterator, List, Optional, Tuple

@dataclasses.dataclass
class GridEnv:
  axis_index: Any
  axis_size: int

_grid_env_stack: List[Tuple[GridEnv, ...]] = []

@contextlib.contextmanager
def grid_env(grid_env: Tuple[Tuple[Any, int], ...]) -> Iterator[None]:
  _grid_env_stack.append(tuple(GridEnv(axis_index, axis_size)
                               for axis_index, axis_size in grid_env))
  yield
  _grid_env_stack.pop()

def current_grid_env() -> Optional[Tuple[GridEnv, ...]]:
  if not _grid_env_stack:
    return None
  return _grid_env_stack[-1]