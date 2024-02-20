<p align="center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 200px;">
  <img src="https://res.cloudinary.com/deztgvefu/image/upload/v1706426486/template_images/cute-little-pink-cat-watercolor-png_2_kxmwtq.webp" alt="Project Logo" width="200">
</p>

# <p align="center">*DjangoE-commerceWebsite*</p>

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
*Welcome to our Online Jewelry Store built with Django! This web application serves as a platform for showcasing and selling a stunning collection of exquisite jewelry. With a user-friendly interface and seamless navigation, customers can explore, select, and purchase their favorite pieces effortlessly..* 

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Built With
<table align="center">
  <tr>
    <td align="center"><img alt="Dj" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg"/></td>
    <td align="center"><img alt="Docker" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg"/></td>
    <td align="center"><img alt="PostgreSQL" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg"/></td>
    <td align="center"><img alt="Redis" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original-wordmark.svg"/></td>
    <td align="center"><img alt="HTML5" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg"/></td>
    <td align="center"><img alt="CSS" width="80px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg"/></td>
  </tr>
</table>

---

1. Deployment:
- Hosted on Amazon Web Services (AWS)
2. Databases:
- PostgreSQL: Optimized CRUD operations, pre-fetched data, and dynamic filtration.
- Redis: Enhanced performance through caching. Implemented sessions for non-registered users to add products to their shopping carts and temporarily store customer wishlist.
3. Backend:
- Followed Django Model View Template (MVT) architecture.
4. Frontend:
- Styled the user interface with CSS for an intuitive shopping experience tailored for desktop users.
###### <p align="center">*Note: Currently optimized for desktop; future plans include implementing media queries for responsiveness on various devices.*</p>
5. User Models:
- Implemented two distinct user models: one for logging credentials and another for personal details.
6. Asynchronous Operations:
- Utilized Celery for background tasks, specifically for cleaning expired shopping carts and managing inventory updates.
7. OOP & SOLID:
- Applied Object-Oriented Programming principles and SOLID for modular and maintainable code.
8. Test Coverage:
- [![Coverage Status](https://img.shields.io/badge/coverage-86%25-brightgreen.svg)](./coverage/index.html){:target="_blank"}



<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Features 

#### I. End Users

1. User Registration and Authentication Pages:
-  Registration:
  
    Users can initiate the registration process by clicking on the dedicated "Register" button in the header. This action redirects them to a new page where they can provide only Login information to create an account. After successful registration, users are directly logged in. Clicking on the user icon redirects users to a new page where they can view and update personal information or delete the user profile. 

- Guest Users:
  
    For users who are not logged in, the user icon redirects them to a new page that encourages them to register or log in.

2. Dynamic Navigation Bar:

    The project features a dynamic navigation bar at the header, providing an intuitive and seamless user experience. The dropdown menu options are dynamically generated from the database, ensuring that any changes or additions are automatically reflected in the menu.

3. Advanced Product Filtering and Real-time Availability Tracking:
   
     When a customer selects a category from the dropdown menu, they are redirected to the chosen category page. Here, an advanced product filtering system awaits, allowing users to refine their search further. The selection menu not only filters the displayed products based on user preferences but also dynamically adjusts other checkboxes based on the available products. A counter is placed next to each checkbox within the Django multiple checkboxes form. These counters provide real-time feedback, indicating the exact number of products available for each checkbox selection.

4. Search:
   
     The search button allows users to input keywords or phrases, and in real-time, it dynamically displays related products from our extensive database. This feature ensures a seamless and efficient browsing experience, helping users find exactly what they are looking for with ease.

5. Like:
   
     For non-registered users, their likes are stored temporarily in the session, allowing them to enjoy a personalized experience during their current visit. Registered users benefit from a seamless experience as their likes are securely stored in the database, ensuring that their preferences are maintained across sessions.

6. Last Seen Products:
   
     As part of our user-centric approach, the system stores the last three products viewed by users in their session. This recent product history is thoughtfully displayed on pages where it is most relevant, ensuring a personalized and efficient browsing experience. Users can easily revisit and consider these recently viewed products, adding a layer of convenience to their journey throughout the platform.

7. Shopping Cart:
   
     Items added to the shopping cart are stored in the session, ensuring a seamless and personalized experience for both logged-in and non-logged-in users.

     To enhance efficiency, our system utilizes Celery to automate the cleanup process. Expired shopping carts are systematically cleared within one hour, returning the products back to the inventory. This not only optimizes the shopping experience but also ensures that the inventory remains accurate and up-to-date.

   After successfully adding items to the shopping bag, customers are redirected to their personalized shopping cart. This feature-rich page provides a detailed overview, including information about the quantity of each product, the total price based on the selected quantity, and the overall order total.

    Customers have the flexibility to adjust the quantity directly on the shopping cart page. Increasing or decreasing the quantity dynamically updates both the displayed total price and the inventory quantity in real-time.
    
    For added convenience, if a product is added for a first or a second time from the product page, a quantity of one is automatically appended. Conversely, using the 'Update Quantity' button to set the quantity to zero removes the product from the shopping cart. Customers can also add as much quantity as available in the inventory, ensuring a flexible and tailored shopping experience.

8. Size Selection:
   
     To enhance the shopping experience, a radio select button must be chosen before adding items to the shopping bag. This ensures clarity and precision in product selection, allowing customers to effortlessly specify their preferences before proceeding to the checkout.

9. Secure Checkout Process: Providing Essential Personal Details:
   
     Upon clicking on the 'Checkout' button, customers are redirected to a page where they can enter their essential personal details, including names, phone number, and delivery address. This mandatory step, ensures that customers provide the necessary information before proceeding.

10. Payment Confirmation with Valid Card Details:
   
     Proceeding to the next step in the checkout process, customers are required to provide valid card details to complete the payment. This ensures a secure and reliable transaction, adhering to industry standards for payment processing.

11. Order Confirmation and Details:
   
     After the successful completion of the payment transaction, customers are redirected to an Order Details page, providing a comprehensive overview of their purchase. This page meticulously lists each product's characteristics, individual total price, and the overall total order price.

    Included in this detailed confirmation is a unique Order ID for reference. Users will also find a summary of their personal information, ensuring transparency and facilitating future reference. The Order Confirmation and Details page serves as a comprehensive receipt, offering customers a complete understanding of their purchase and order specifics.

12. Order History:
   
     Registered users can enjoy a shopping experience with the added convenience of an order history feature. Every purchase made by a registered user is meticulously recorded and stored, allowing them to effortlessly track their order history.

14. Pagination:
   
     To enhance accessibility, large sets of content are broken down into manageable sections. Users can effortlessly navigate through pages, ensuring a user-friendly and efficient exploration of our extensive collection. 

15. Enhanced Form Display: Customizing Labels and Utilizing Placeholders:
   
     In this implementation, default Django form labels have been removed, creating a cleaner and more streamlined appearance. Instead, placeholders have been implemented, offering users intuitive cues within the form fields. This enhancement not only improves aesthetics but also ensures a more user-friendly and modern form interaction.

16. User-Friendly Error Messages:
   
     Enhancing user experience, our system features custom error messages that provide clear and concise feedback. These messages are designed to be user-friendly, allowing customers to easily understand and address any issues that may arise. Notably, these error messages are conveniently dismissible with a simple click, ensuring a seamless and non-intrusive interaction.

17. Logout Functionality:
   
     By clicking on the Logout button conveniently placed in the header, customers can initiate alog-out process. Following the click, users are redirected to the Login or Register page.

#### II. Admin Users

1. User Model:
- Customizes the Django admin interface for user accounts.
- Disables the delete permission for user objects.
- Defines ordering, list display, search fields, and fieldsets for user details.
- Implements a custom add form using the AccountProfileForm.
- Includes fields for email, password, permissions, and important dates.

2. Profile Model:
- Customizes the Django admin interface for user profiles.
- Defines read-only fields for user details.
- Specifies list display, ordering, list filter, search fields, and sortable fields.
- Organizes fields into fieldsets based on personal information, contact details, and delivery address.

3. Jewelries Model:
- Customizes the Django admin interface for jewelry products.
- Defines list display, list filter, search fields, and inlines for associated models (metals, stones, sizes).
- Implements custom methods to display metals, stone types, and stone colors in the list view.

3. Inventory Model:
- Customizes the Django admin interface for inventory management.
- Specifies list display, ordering, list filter, search fields, and sortable fields.
- Organizes fields into fieldsets based on jewelry, quantity, and price details.


<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BeatrisIlieve/DjangoE-commerceWebsite.git
    cd DjangoE-commerceWebsite
    ```

2. Install Docker:

    Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) to install Docker on your machine.

3. Build and start the Docker container for PostgreSQL:

    Follow the [official guide on how to use the Postgres Docker Official Image](https://hub.docker.com/_/postgres) to run the PostgreSQL Docker Container.


4. Build and start the Docker container for Redis:

    Follow the [official guide on how to use the Redis Docker Official Image](https://hub.docker.com/_/redis) to run the Redis Docker Container.

5. Install the project dependencies using [pip](https://pip.pypa.io/en/stable/):

    ```bash
    pip install -r requirements.txt
    ```
6. Run Celery worker:

    ```bash
    celery -A e_commerce_website worker -l info
    ```

7. Run Celery Beat in a separate terminal:

    ```bash
    celery -A e_commerce_website beat -l info
    ```

8. Apply database migrations:

    ```bash
    python manage.py migrate
    ```
    
9. Run [populate_base_tables.py](populate_base_tables.py)

10. Run [populate_jewelries.py](populate_jewelries.py)

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Usage
1. Run the development server:

    ```bash
    python manage.py runserver
    ```
  
2. Visit [localhost:8000](http://localhost:8000) in your web browser to access the Django application.

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## Entity Relationship Diagram:
![diagram](https://github.com/BeatrisIlieve/DjangoE-commerceWebsite/assets/122045435/9be83e6b-b8f3-410c-bed4-495924d5409c)

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

## License
This project is licensed under the [MIT License](LICENSE).

<p align="right" dir="auto"><a href="#djangoe-commercewebsite">Back To Top</a></p>

