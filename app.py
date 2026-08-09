import os
from calle import CalleClient

client = CalleClient(api_key=os.environ.get("CALLE_API_KEY"))

def run_appointment_agent(customer_name: str, phone_number: str, appointment_time: str):
    """
    Runs an autonomous phone agent to confirm or reschedule appointments.
    """
    print(f"Starting agent call for {customer_name} ({phone_number})...")
    
    task_prompt = (
        f"Call {phone_number}. You are a professional, polite scheduling assistant. "
        f"Politely speak with {customer_name} and confirm if they can attend their upcoming appointment scheduled for {appointment_time}. "
        f"If they confirm, thank them and wrap up. If they need to reschedule, ask for their preferred new date and time. "
        f"Ensure you gather their final confirmation status and any newly requested time slot."
    )

    try:
        response = client.calls.create_and_wait(task=task_prompt)
        
        print("\n--- Agent Call Session Finished ---")
        print(f"Call ID: {response.get('id')}")
        print(f"Overall Status: {response.get('status')}")
        print(f"Summary of Call: {response.get('summary')}")
        
        # Check specific recipient results if available
        recipients = response.get('recipients', [])
        if recipients:
            for rec in recipients:
                print(f"Recipient Phone: {rec.get('phones')}")
                print(f"Attempt Status: {rec.get('status')}")
                print(f"Structured Result: {rec.get('structured_result')}")
                
        return response

    except Exception as e:
        print(f"Error executing agent workflow: {e}")

if __name__ == "__main__":
    # Test execution using your sandbox test flow
    run_appointment_agent(
        customer_name="Jane Doe",
        phone_number="+14155552671",
        appointment_time="Monday at 10:00 AM"
    )