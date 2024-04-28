<a name="django-gems"></a>

<p align="center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 200px;">
  <img src="https://res.cloudinary.com/deztgvefu/image/upload/v1707852478/template_images/Screenshot_2024-02-13_at_21.27.06_exrwvw.png" alt="Project Logo" width="340">
</p>

---
<br>

### <p align="center"> *Visit our online store:<br> ec2-13-36-51-60.eu-west-3.compute.amazonaws.com* </p>

<br>

---

<a name="built-with"></a>
<a name="entity-relationship-diagram"></a>

<h4 align="center">
  <a href="#introduction">Introduction</a> ·
  <a href="#demo-video">Demo Video</a> ·
  <a href="#built-with">Built With</a> ·
  <a href="#features">Features</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#entity-relationship-diagram">Entity Relationship Diagram</a> ·
  <a href="#license">License</a>
</h4>

---

## Introduction
<p><i>Welcome to our Online Jewelry Store! This web application serves as a platform for showcasing and selling a stunning collection of exquisite jewelry. With a user-friendly       interface and seamless navigation, customers can explore, select, and purchase their favorite pieces effortlessly..</i></p>

<br>

## Demo Video

[![Watch the video](https://img.youtube.com/vi/KnK5HedIVjo/maxresdefault.jpg)](https://www.youtube.com/embed/KnK5HedIVjo)

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

## Built With
<table align="center">
  <tr>
    <td align="center"><img alt="Dj" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg"/></td>
    <td align="center"><img alt="Docker" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg"/></td>
    <td align="center"><img alt="PostgreSQL" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg"/></td>
    <td align="center"><img alt="HTML5" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg"/></td>
    <td align="center"><img alt="CSS" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg"/></td>
    <td align="center"><img alt="AWS" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"/></td>
  </tr>
</table>

<br>

1. #### Backend:
- Followed Django Model View Template (MVT) architecture.
2. #### Databases:
- PostgreSQL: Optimized CRUD operations, pre-fetched data, and dynamic filtration.
3. #### Frontend:
- Styled the user interface with CSS for an intuitive shopping experience tailored for desktop users.
> [!NOTE]
> Currently optimized for desktop; future plans include implementing media queries for responsiveness on various devices.
4. #### OOP & SOLID:
- Applied Object-Oriented Programming principles and SOLID for modular and maintainable code.
5. #### Deployment:
- Hosted on Amazon Web Services (AWS).
6. #### Test Coverage:
- [![Coverage Status](https://img.shields.io/badge/coverage-81%25-brightgreen.svg)](./coverage/index.html)

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

## Features 

1. #### User Models:
- Implemented two distinct user models:
  - logging credentials
  - personal details
    
- Change Email functionality
- Change Password functionality
- Change Personal Details functionality
- Detele Profile functionality
- Logout functionality

2. #### Dynamic Navigation Bar:
- The dropdown menu options are dynamically generated from the database, ensuring that any changes or additions are automatically reflected in the menu.

3. #### Advanced Product Filtering and Real-time Availability Tracking:
- When a customer selects a choice from the dropdown menu, they are redirected to the chosen page.
- Here, an advanced product filtering system awaits, allowing users to refine their search further.
  - The selection menu not only filters the displayed products based on user preferences but also dynamically adjusts other checkboxes based on the available products.
  - A counter is placed next to each checkbox within the Django multiple checkboxes form. These counters provide real-time feedback, indicating the exact number of products available for each checkbox selection.

4. #### Shopping Cart:
##### Adding to Cart:
- After successfully adding items to the shopping bag, customers are redirected to their personalized shopping cart. This page provides a detailed overview, including information about the quantity of each product, the total price based on the selected quantity, and the overall order total.
  
- Customers have the flexibility to adjust the quantity directly on the shopping cart page. Increasing or decreasing the quantity dynamically updates both the displayed total price and the inventory quantity in real-time.
- For added convenience, if a product is added for a first or a second time from the product page, a quantity of one is automatically appended. Conversely, using the 'Update Quantity' button to set the quantity to zero removes the product from the shopping cart. Customers can also add as much quantity as available in the inventory, ensuring a flexible and tailored shopping experience.
- Non-registered users can add items to their shopping cart without creating an account. 
  - When users add items to their shopping cart, a cart is created in our database and linked to their current session key. This session key serves as a temporary identifier.
  - Our system is designed with dedicated settings and functions to ensure that the session key remains associated with the user's cart and account even after completing the registration process.
  - After a customer completes the registration, they will be redirected back to their shopping cart. All the items they had selected before registering will still be there, ready for them to proceed with their purchase.
##### Purchase Process:
- Upon clicking on the 'Checkout' button, customers are redirected to a page where they can enter their essential personal details, including names, phone number, and delivery address. This mandatory step, ensures that customers provide the necessary information before proceeding.
- Proceeding to the next step in the checkout process, customers are required to provide valid card details to complete the payment. This ensures a secure and reliable transaction, adhering to industry standards for payment processing.

5. #### Search:
   
     The search button allows users to input keywords or phrases, and in real-time, it dynamically displays related products from our extensive database.

6. #### Wishlist:
   
     For non-registered users, their likes are stored temporarily in the session, allowing them to enjoy a personalized experience during their current visit. Registered users benefit from having their likes stored in the database, ensuring that their preferences are maintained across sessions.

7. #### Last Seen Products:
   
     The system stores the last three products viewed by users in their session. This recent product history is displayed on pages where it is most relevant. Users can easily revisit and consider these recently viewed products, by clicking on them.

8. #### Size Selection:
   
     A radio select button must be chosen before adding items to the shopping bag. This ensures clarity and precision in product selection, allowing customers to specify their preferences before proceeding to the checkout.

9. #### Order Confirmation and Details:
   
     After the successful completion of the payment transaction, customers are redirected to an Order Details page, providing a comprehensive overview of their purchase. This page lists each product's characteristics, individual total price, and the overall total order price.

    Included in this detailed confirmation is a unique Order ID for reference. Users will also find a summary of their personal information, ensuring transparency and facilitating future reference. 

10. #### Order History:
   
     Registered users can enjoy a shopping experience with the added convenience of an order history feature. Every purchase made by a registered user is recorded and stored, allowing them to effortlessly track their order history.

11. #### Pagination:
   
     Users can effortlessly navigate through pages, ensuring a user-friendly and efficient exploration of our extensive collection. 

12. #### Enhanced Form Display: Customizing Labels and Utilizing Placeholders:
   
     In this implementation, default Django form labels have been removed, creating a cleaner and more aesthetic appearance. Instead, placeholders have been implemented, offering users intuitive cues within the form fields.

13. #### User-Friendly Error Messages:
   
     Our system features custom error messages that provide clear and concise feedback. Notably, these error messages are conveniently dismissible with a simple click, ensuring a non-intrusive interaction.

14. #### Email Notifications:
- Upon successful registration on our platform, users will receive a confirmation email. This email includes a button that, when clicked, will direct users to our website.
- After a successful purchase, users will receive a purchase confirmation email.

## Installation

1. #### Clone the repository:

    ```bash
    git clone https://github.com/BeatrisIlieve/DjangoGems.git
    ```

2. #### Install Docker:

    Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) to install Docker on your machine.

3. #### Build and start the Docker container for PostgreSQL:

    Follow the [official guide on how to use the Postgres Docker Official Image](https://hub.docker.com/_/postgres) to run the PostgreSQL Docker Container.


4. #### Install the project dependencies using [pip](https://pip.pypa.io/en/stable/):

    ```bash
    pip install -r requirements.txt
    ```

5. #### Apply database migrations:

    ```bash
    python manage.py migrate
    ```
    
6. #### Populate the database with jewelry data by running the following command:

    ```bash
    python manage.py initialize_jewelries_data
    ```

7. #### Initialize the database with specific quantities and prices for each jewelry item using the following command:

    ```bash
    python manage.py initialize_inventory_data
    ```

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

## Usage
1. #### Run the development server:

    ```bash
    python manage.py runserver
    ```
  
2. #### Visit [localhost:8000](http://localhost:8000) in your web browser to access the Django application.

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

## Entity Relationship Diagram:
![diagram](https://github.com/BeatrisIlieve/DjangoE-commerceWebsite/assets/122045435/9be83e6b-b8f3-410c-bed4-495924d5409c)

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

## License
This project is licensed under the [MIT License](LICENSE).

<p align="right" dir="auto"><a href="#django-gems">Back To Top</a></p>

