def format_feedback(customer_name,feedback):
    customer_name = customer_name.strip().title()
    feedback= feedback.strip()

    if feedback:
        feedback=feedback[0].upper()+feedback[1:]

        feedback=feedback.replace("can't", "can not")
        feedback=feedback.replace("won't", "will not")

    formatted_message = (
        f"customer name:{customer_name}\n"
        f"feedback:{feedback}\n"
        f"thankyou , {customer_name},for sharing your variable feedback..."
    )

    return formatted_message
name = input("Enter customer name :")
feedback = input("Enter customer feedback :")

result = format_feedback(name, feedback)

print("\n =======format customer feedback=======")
print(result)