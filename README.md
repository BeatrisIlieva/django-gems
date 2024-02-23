<p align="center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 200px;">
  <img src="https://res.cloudinary.com/deztgvefu/image/upload/v1706426486/template_images/cute-little-pink-cat-watercolor-png_2_kxmwtq.webp" alt="Project Logo" width="200">
</p>

# <p align="center">*DjangoGems*</p>

<p style="
        max-width: 620px;
        font-size: 16px;
        padding-left: 3%;
        padding-right: 3%;
        padding-bottom: 2%;
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">
    <a href="http://ec2-15-236-82-16.eu-west-3.compute.amazonaws.com"
       style="
           display: inline-block;
           padding: 10px 20px;
           background-color: #f38ab7; color: #fff;
           text-decoration: none;
           border-radius: 5px;">
        http://ec2-15-236-82-16.eu-west-3.compute.amazonaws.com
    </a>
</p>

<a name="built-with"></a>
<a name="entity-relationship-diagram"></a>


<p align="center">
  <a href="#introduction">Introduction</a> ·
  <a href="#built-with">Built With</a> ·
  <a href="#features">Features</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#entity-relationship-diagram">Entity Relationship Diagram</a> ·
  <a href="#license">License</a>
</p>

## Introduction
*Welcome to our Online Jewelry Store! This web application serves as a platform for showcasing and selling a stunning collection of exquisite jewelry. With a user-friendly interface and seamless navigation, customers can explore, select, and purchase their favorite pieces effortlessly..* 

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

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

---
1. #### Backend:
- Followed Django Model View Template (MVT) architecture.
2. #### Databases:
- PostgreSQL: Optimized CRUD operations, pre-fetched data, and dynamic filtration.
- Redis: Enhanced performance through caching. Implemented sessions for non-registered users to add products to their shopping carts and temporarily store customer wishlist.
3. #### Frontend:
- Styled the user interface with CSS for an intuitive shopping experience tailored for desktop users.
###### <p align="center">*Note: Currently optimized for desktop; future plans include implementing media queries for responsiveness on various devices.*</p>
4. #### User Models:
- Implemented two distinct user models: one for logging credentials and another for personal details.
5. #### OOP & SOLID:
- Applied Object-Oriented Programming principles and SOLID for modular and maintainable code.
6. #### Deployment:
- Deployed Django website on AWS for efficient and simplified hosting.
7. #### Test Coverage:
- [![Coverage Status](https://img.shields.io/badge/coverage-81%25-brightgreen.svg)](./coverage/index.html)


<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Features 

### I. End Users

1. #### Shopping Cart and User Registration

    Items added to the shopping cart are stored in the session, ensuring a seamless and personalized experience for both logged-in and non-logged-in users.

#### Guest Checkout

- **Adding to Cart:**
  Non-registered users can add items to their shopping cart without creating an account. The selected items will be stored in the session.

- **Purchase Process:**
  To complete a purchase, users need to register, providing personal details and valid card information during the checkout process.

#### User Registration

- **Registration Redirect:**
  After successful registration, users are automatically redirected back to their shopping cart. This allows them to view and proceed with the purchase of the jewelries already added to their cart.

- **Seamless Experience:**
  This seamless integration between user registration and the shopping cart ensures a smooth transition for users, maintaining the items they've added before registering.

###### <p align="center">*Please note that completing the registration process is necessary for finalizing the purchase and ensuring a secure transaction.*</p>

#### Shopping Cart

To enhance efficiency, our system utilizes Celery to automate the cleanup process. Expired shopping carts are systematically cleared within one hour, returning the products back to the inventory. This not only optimizes the shopping experience but also ensures that the inventory remains accurate and up-to-date.

After successfully adding items to the shopping bag, customers are redirected to their personalized shopping cart. This feature-rich page provides a detailed overview, including information about the quantity of each product, the total price based on the selected quantity, and the overall order total.

Customers have the flexibility to adjust the quantity directly on the shopping cart page. Increasing or decreasing the quantity dynamically updates both the displayed total price and the inventory quantity in real-time.

For added convenience, if a product is added for a first or a second time from the product page, a quantity of one is automatically appended. Conversely, using the 'Update Quantity' button to set the quantity to zero removes the product from the shopping cart. Customers can also add as much quantity as available in the inventory, ensuring a flexible and tailored shopping experience.

2. #### Dynamic Navigation Bar:

    The project features a dynamic navigation bar at the header, providing an intuitive and seamless user experience. The dropdown menu options are dynamically generated from the database, ensuring that any changes or additions are automatically reflected in the menu.

3. #### Advanced Product Filtering and Real-time Availability Tracking:
   
     When a customer selects a category from the dropdown menu, they are redirected to the chosen category page. Here, an advanced product filtering system awaits, allowing users to refine their search further. The selection menu not only filters the displayed products based on user preferences but also dynamically adjusts other checkboxes based on the available products. A counter is placed next to each checkbox within the Django multiple checkboxes form. These counters provide real-time feedback, indicating the exact number of products available for each checkbox selection.

4. #### Search:
   
     The search button allows users to input keywords or phrases, and in real-time, it dynamically displays related products from our extensive database. This feature ensures a seamless and efficient browsing experience, helping users find exactly what they are looking for with ease.

5. #### Wishlist:
   
     For non-registered users, their likes are stored temporarily in the session, allowing them to enjoy a personalized experience during their current visit. Registered users benefit from a seamless experience as their likes are securely stored in the database, ensuring that their preferences are maintained across sessions.

6. #### Last Seen Products:
   
     As part of our user-centric approach, the system stores the last three products viewed by users in their session. This recent product history is thoughtfully displayed on pages where it is most relevant, ensuring a personalized and efficient browsing experience. Users can easily revisit and consider these recently viewed products, adding a layer of convenience to their journey throughout the platform.



7. #### Size Selection:
   
     To enhance the shopping experience, a radio select button must be chosen before adding items to the shopping bag. This ensures clarity and precision in product selection, allowing customers to effortlessly specify their preferences before proceeding to the checkout.

8. #### Secure Checkout Process: Providing Essential Personal Details:
   
     Upon clicking on the 'Checkout' button, customers are redirected to a page where they can enter their essential personal details, including names, phone number, and delivery address. This mandatory step, ensures that customers provide the necessary information before proceeding.

9. #### Payment Confirmation with Valid Card Details:
   
     Proceeding to the next step in the checkout process, customers are required to provide valid card details to complete the payment. This ensures a secure and reliable transaction, adhering to industry standards for payment processing.

10. #### Order Confirmation and Details:
   
     After the successful completion of the payment transaction, customers are redirected to an Order Details page, providing a comprehensive overview of their purchase. This page meticulously lists each product's characteristics, individual total price, and the overall total order price.

    Included in this detailed confirmation is a unique Order ID for reference. Users will also find a summary of their personal information, ensuring transparency and facilitating future reference. The Order Confirmation and Details page serves as a comprehensive receipt, offering customers a complete understanding of their purchase and order specifics.

11. #### Order History:
   
     Registered users can enjoy a shopping experience with the added convenience of an order history feature. Every purchase made by a registered user is meticulously recorded and stored, allowing them to effortlessly track their order history.

12. #### Pagination:
   
     To enhance accessibility, large sets of content are broken down into manageable sections. Users can effortlessly navigate through pages, ensuring a user-friendly and efficient exploration of our extensive collection. 

13. #### Enhanced Form Display: Customizing Labels and Utilizing Placeholders:
   
     In this implementation, default Django form labels have been removed, creating a cleaner and more streamlined appearance. Instead, placeholders have been implemented, offering users intuitive cues within the form fields. This enhancement not only improves aesthetics but also ensures a more user-friendly and modern form interaction.

14. #### User-Friendly Error Messages:
   
     Enhancing user experience, our system features custom error messages that provide clear and concise feedback. These messages are designed to be user-friendly, allowing customers to easily understand and address any issues that may arise. Notably, these error messages are conveniently dismissible with a simple click, ensuring a seamless and non-intrusive interaction.

15. #### Change Email Functionality

16. #### Change Password Functionality

17. #### Change Personal Details Functionality

18. #### Detele Profile Functionality

19. #### Logout Functionality

20. #### Email Notifications:
- Upon successful registration on our platform, users will receive a confirmation email. This email includes a button that, when clicked, will direct users to our website.
- After a successful purchase, users will receive a purchase confirmation email. This email includes a button that, when clicked, directs users to their order history on our website.
    

### II. Admin Users
The admin interface is designed to facilitate the complete addition of jewelry items effortlessly.

1. #### User Model:
The user model is customized to handle user accounts. In the admin panel, you can manage user details, including email, password, permissions, and important dates.

2. #### Profile Model:
The account profile model contains information related to user profiles, including personal details, contact information, and delivery addresses. Users can manage their profiles seamlessly through the admin panel.

3. #### Jewelry Models:
##### Jewelry
The main jewelry model includes details like title, category, metals, stone types, and stone colors. You can completely add a jewelry item through the user-friendly admin panel. The admin panel features filtration, ordering, and search options for efficient management.

###### Filtration and Ordering
- Filter by category, metals, stone types, and stone colors
- Order by title or any relevant attribute

###### Search
- Search for jewelry items based on their title.

###### Admin Sections
- The admin pages are structured into sections using fieldsets, allowing for an organized and intuitive experience when managing jewelry items

##### Category, Metal, GoldCaratWeight, StoneType, StoneColor, Size
These models represent categories, metals, gold carat weights, stone types, stone colors, and sizes respectively. The admin panels for each model allow easy management of these entities.

##### JewelryMetal, JewelryStone, JewelrySize
These models handle the relationships between jewelry and metals, stones, and sizes respectively. The admin panels for these models make it easy to manage these associations.

4. #### Inventory
The inventory model is designed for keeping track of jewelry quantities and prices. The admin interface provides options to manage inventory efficiently, including features for jewelry, quantity, and pricing.

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Installation

1. #### Clone the repository:

    ```bash
    git clone https://github.com/BeatrisIlieve/DjangoGems.git
    ```

2. #### Install Docker:

    Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) to install Docker on your machine.

3. #### Build and start the Docker container for PostgreSQL:

    Follow the [official guide on how to use the Postgres Docker Official Image](https://hub.docker.com/_/postgres) to run the PostgreSQL Docker Container.


4. #### Build and start the Docker container for Redis:

    Follow the [official guide on how to use the Redis Docker Official Image](https://hub.docker.com/_/redis) to run the Redis Docker Container.

5. #### Install the project dependencies using [pip](https://pip.pypa.io/en/stable/):

    ```bash
    pip install -r requirements.txt
    ```
6. #### Run Celery worker:

    ```bash
    celery -A e_commerce_website worker -l info
    ```

7. #### Run Celery Beat in a separate terminal:

    ```bash
    celery -A e_commerce_website beat -l info
    ```

8. #### Apply database migrations:

    ```bash
    python manage.py migrate
    ```
    
9. #### Populate the database with jewelry data by running the following command:

    ```bash
    python manage.py initialize_jewelries_data
    ```

10. #### Initialize the database with specific quantities and prices for each jewelry item using the following command:

    ```bash
    python manage.py initialize_inventory_data
    ```

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Usage
1. #### Run the development server:

    ```bash
    python manage.py runserver
    ```
  
2. #### Visit [localhost:8000](http://localhost:8000) in your web browser to access the Django application.

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Entity Relationship Diagram:
![diagram](https://github.com/BeatrisIlieve/DjangoE-commerceWebsite/assets/122045435/9be83e6b-b8f3-410c-bed4-495924d5409c)

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## License
This project is licensed under the [MIT License](LICENSE).

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

