# GraphScheduling

## Project Description
**GraphScheduling** is a tool designed to visualize and analyze scheduling graphs. It checks if a given graph has any circuits (cycles). If no circuits are found, it confirms that the scheduling graph is valid. The tool also provides interactive features like zooming and toggling view modes, making it easier to navigate complex scheduling data.

---

## Graph Visualization
- **Status**: “No circuit detected” serves as an example outcome indicating a valid scheduling graph.
- **Features**:
  - **Zoom**: Zoom in/out to analyze parts of the graph more closely.
  - **View Mode**: Switch between different layout modes or levels of detail.

---

## Example Value Matrix
Below is an **example** matrix representing task relationships and dependencies. The symbol “∴” denotes an undefined or non-existent relationship. In practice, you would replace this example with the actual data for your project.

|     | α   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | ω   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **α**   | ∴   | 0   | 0   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **1**   | ∴   | ∴   | ∴   | 2   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **2**   | ∴   | ∴   | ∴   | ∴   | 5   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **3**   | ∴   | ∴   | ∴   | ∴   | 4   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **4**   | ∴   | ∴   | 4   | ∴   | ∴   | ∴   | ∴   | ∴   | 2   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **5**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 2   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **6**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 5   | ∴   | ∴   | ∴   | ∴   | ∴   | 5   | ∴   |
| **7**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 9   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **8**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 2   | ∴   | ∴   | ∴   | ∴   | ∴   |
| **9**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 5   |
| **10**  | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 1   |
| **11**  | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 1   | ∴   | ∴   | ∴   | ∴   |
| **12**  | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 1   | ∴   |
| **13**  | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | 9   |
| **ω**   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   | ∴   |

---

## Example Calendar and Margins
The table below is an **example** of how task scheduling information can be presented. It includes earliest start times, latest start times, total float, and free float for each task. Replace this data with your actual schedule when using GraphScheduling in production.

| Task  | Earliest Start | Latest Start | Total Float | Free Float |
|-------|----------------|--------------|-------------|------------|
| 1     | 0              | 0            | 0           | 0          |
| 2     | 0              | 0            | 0           | 0          |
| 3     | 0              | 1            | 1           | 0          |
| 4     | 2              | 2            | 0           | 0          |
| 5     | 6              | 6            | 0           | 0          |
| 6     | 8              | 8            | 0           | 0          |
| 7     | 13             | 13           | 0           | 0          |
| 8     | 18             | 18           | 0           | 0          |
| 9     | 27             | 27           | 0           | 0          |
| 10    | 29             | 29           | 0           | 0          |
| 11    | 9              | 33           | 24          | 0          |
| 12    | 8              | 8            | 0           | 0          |
| 13    | 6              | 24           | 18          | 0          |
| 14    | 18             | 25           | 7           | 0          |
| 15    | 34             | 34           | 0           | 0          |

---

## Usage
1. **Load Data**: Import your scheduling data into the GraphScheduling tool.
2. **Analyze Graph**: Check the graph to confirm no circuits exist.
3. **Review Relationships**: Use the matrix (or equivalent data structure) to see how tasks interrelate.
4. **Consult Schedule**: Inspect the calendar to see earliest/latest start times and float values.
5. **Adjust & Optimize**: Update task dependencies and durations based on findings to optimize the schedule.

---

## Contributing
You can contribute by:
- Reporting issues or bugs.
- Suggesting new features.
- Submitting pull requests with improved or additional functionalities.

---

## License
This project is provided under an open license. For more details, consult the `LICENSE` file.

---

Thank you for using **GraphScheduling**!
