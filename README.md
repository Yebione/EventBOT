# EventBOT - AI-Powered Event Planning

EventBOT is a simple and intuitive Streamlit application designed to help organizations effortlessly plan events using the Google Generative AI API. With just a few inputs, EventBOT generates a comprehensive event plan, ensuring a smooth and well-organized event experience.

## Features

- **User-Friendly Interface**: Easy-to-use Streamlit interface with a sleek sidebar for inputting event details.
- **AI-Powered Planning**: Utilizes the Google Generative AI API to generate detailed event plans.
- **Comprehensive Event Plans**: Outputs include event name, date, venue, participants, overview, program flow, objectives, needed materials/resources with prices, and a conclusion.
- **Structured Layout**: Ensures the event plan is well-structured and presentable, ready to be shared with stakeholders.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/eventbot.git
    cd eventbot
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Google API key**:
    - Create a `.env` file in the project directory.
    - Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=your_google_api_key_here
        ```

## Usage

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Input Event Details**:
    - Provide the name of your event.
    - Specify the date (Month-Day-Year).
    - Enter the venue of the event.
    - List the target participants (separated by commas).
    - Describe the expected activities (separated by commas).

3. **Generate Event Plan**:
    - Click the 'Submit' button.
    - View the generated event plan on the main screen.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any inquiries or feedback, please contact:
- **Kyle Billones**: [kyle.billones@wvsu.edu.ph]

---

**EventBOT** is here to simplify your event planning process, harnessing the power of Google Generative AI to create tailored event plans with ease. Perfect for event organizers, community managers, and anyone looking to host a memorable event.

Enjoy seamless event planning with EventBOT!
