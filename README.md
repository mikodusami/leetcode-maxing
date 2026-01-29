# General Coding Assessment Strategy 

**GOAL:** Do not write a single line of code until Step 5 is complete.

### 0. Pattern Recognition
* **Scan:** Read the problem entirely.
* **Identify:** Is this *Optimization* (min/max), *Counting* (how many), *Search* (find specific), or *Transformation* (sort/rotate)?
* **Keywords:** Write down triggers (e.g., "sorted" → Binary Search/Two Pointer, "shortest path" → BFS).

### 1. The I/O Contract
* **Input:** Exactly what data enters? (e.g., `Input: int[][] grid, int k`)
* **Output:** Exactly what data leaves? (e.g., `Output: int (min_steps)`)
* **Visual:** Draw the simplest possible example case.

### 2. The Strategic Split (CRITICAL)
**Question:** "Does a choice I make now restrict or change my available choices in the future?"

#### **PATH A: YES (Branching / Multiverse)**
* *Topics: DP, Backtracking, Graphs, Recursion*
* **State Definition:** "If I pause the program, what specific variables do I need to save to resume later?"
* **Overlap Check:** "Will I solve the exact same sub-problem multiple times?" (Yes = Memoization).

#### **PATH B: NO (Linear / Deterministic)**
* *Topics: Greedy, Two-Pointer, Sliding Window, Heap*
* **Reduction:** "Can I rule out a section of the input based on a simple condition?"
* **Greedy Proof:** "If I take the immediate best option, is it theoretically impossible for it to be wrong?"

### 3. Defining The Logic
* **For Path A (Transitions):**
    * "What are the distinct 'legal moves' from the current state?"
    * "How do I combine the results? (Min, Max, Sum, OR?)"
    * "What is the Base Case (when do I stop)?"
* **For Path B (Invariants):**
    * "What rule must always remain true?" (e.g., `right > left`)
    * "What specific condition forces me to move/update?" (e.g., `if sum < target, left++`)
    * "When does the loop terminate?"

### 4. Constraints & Complexity Check
* **Check:** Compare your logic (Path A or B) against `N`.
    * `N <= 20`: $O(2^n)$ or $O(n!)$ (Backtracking ok)
    * `N <= 10^4`: $O(n^2)$ (DP/Nested Loops ok)
    * `N <= 10^7`: $O(n)$ or $O(n \log n)$ (Must be Greedy/Linear)
* **Verify:** Does your proposed method fit the time limit? If not, return to Step 2.

### 5. The "Chinese Table" (Dry Run)
* **Draw a Table:**
    * *Path A:* Columns = State Variables. Rows = Recursive Steps.
    * *Path B:* Columns = Pointers & Current Values. Rows = Iterations.
* **Trace:** Manually fill the table for the example case.
* **Edge Case:** Does logic hold for Empty Input? Single Element? All Duplicates?
