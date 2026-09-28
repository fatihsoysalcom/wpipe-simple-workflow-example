import wpipe
import time

# Define a simple task that simulates some work
def task_a(input_data):
    print(f"Task A started with: {input_data}")
    time.sleep(1)  # Simulate work
    result = f"Result from A: {input_data.upper()}"
    print("Task A finished")
    return result

# Define another task that depends on the output of the first task
def task_b(input_data):
    print(f"Task B started with: {input_data}")
    time.sleep(1)  # Simulate work
    result = f"Result from B: {input_data} - Processed"
    print("Task B finished")
    return result

# Define a task that runs independently
def task_c(message):
    print(f"Task C started with: {message}")
    time.sleep(0.5) # Simulate work
    print("Task C finished")
    return "C completed"

if __name__ == "__main__":
    # Create a new workflow
    workflow = wpipe.Workflow(name="MySimpleWorkflow")

    # Define tasks and their dependencies
    # Task A is the first task, it has no dependencies
    task_a_node = workflow.add_task(task_a, name="TaskA")

    # Task B depends on Task A's output
    task_b_node = workflow.add_task(task_b, depends_on=task_a_node, name="TaskB")

    # Task C runs independently
    task_c_node = workflow.add_task(task_c, name="TaskC")

    # Define the input data for the workflow
    workflow.set_inputs({
        "TaskA": {"input_data": "hello"},
        "TaskC": {"message": "independent message"}
    })

    # Run the workflow
    print("Starting workflow...")
    workflow.run()
    print("Workflow finished.")

    # You can also access results if needed, though not explicitly shown in this simple example
    # For example: task_b_node.result
