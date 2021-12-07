# ANTONIO TORONE Milestone 4 - Full Stack Frameworks with Django

[View here the live project]()


## HOPPY STOP

Hoppy Stop is an e-commerce site based on the trade-in canned beer with expansion to other beer related products. It is developed for business purposes. The site allows the owner to increase sales and expand their business through the internet. The e-commerce site these days is critically essential for any business also to keep up with the competition. The features included in this project are wholly related to online commerce being known as a shop and expanding their profit by becoming big. It is intuitive, responsive, friendly, and colourful

<h2 align="center"><img src=""></h2>


## User Experience (UX)

### User stories

#### First time visitor goals

1. As a first-time visitor, I want to get to a website that makes me feel like to be in the right place, as in a live beer shop.
2. As a first-time visitor, I want to be able to see what the website can offer me.
3. As a first-time visitor, I want to be able to get a quick and accurate research of a specific product or a specific type of beer.

#### Returning visitor goals

1. As a returning visitor, I want to create a private account.
2. As a returning visitor, I want to see the website more interesting and more inviting.

#### Frequent user goals

1. As a frequent user, I want to be able to see my orders and the amount per any order.
2. As a frequent user, I want to be able to see and read products review.

### Design

#### Color scheme

1. The main colours used around the website are  black, red and white. The black colour is used on the header as a background adompting the linear-gradient effect with  (1deg, black, with the gradient #00000094). The others black elements presents, are the submit form buttons, that have the  default boostrap class black colour and the quantity input. Obviously the others elements are header and they have the black colour by default.

2. The red colour is used for reflect the logo, in fact is used as a hover on the navigation bar for the categories and in product details page for consistency. THe red colour is also present throught the bootstrap class 'danger' that display any content in red.

3. The white colour is used majority as a body background color around the various templates. This colour is perfect for display products because for him cleanliness, freshness, and simplicity.

#### Tipography

The font family chosen is serif. Very simple, very clear and intuitive.

### Imagery

THe images as a e-commerce website are critically important to show the product and they need to be clean and invitant to the user eyes. For study purposes, the beer and cases images has been taken from the website HonestBrew. Plese find here the link to the website  [View-here] (https://honestbrew.co.uk/).
The images regarding the category kegs, has been taken form the website DrinkStation. Please find here the link to the website  [View-here] (https://www.drinkstation.co.uk/).
In the end the images regarding the glasses has been taken from the website Hopt. Please find here the link to the website [View-here] (https://www.hopt.it/) 

### Wireframes

All devices wireframes PDF file [view] ()

## Features

* Directly purposeful
* Intuitive
* Friendly
* tidy

## Technologies used

### Language used

[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)

[JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)

[PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs used

1. [Bootstrap5.0:](https://getbootstrap.com/)

2. [Jquery:](https://jquery.com/)

3. [Django](https://www.djangoproject.com/)

4. [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

5. [Fontawesome:](https://fontawesome.com/)

6. [Stripe:](https://stripe.com/gb)

7. [Aws:](https://aws.amazon.com/)

8. [Photoshop:](https://www.adobe.com/)

9. [Git:](https://git-scm.com/)

10. [Github:](https://github.com/)

11. [Heroku:](https://heroku.com/)

12. [Balsamiq:](https://balsamiq.com/)

13. [Illustrator:](https://www.adobe.com/uk/products/illustrator)

## Testing

### Testing user stories from user experience (UX section)

####  First time visitor

1. As a first-time visitor, I want to get to a website that makes me feel like to be in the right place, as in a live beer shop.

   1. For these user stories, the logo and the carousel slices do the job. The logo is designed with a hopp inside, the leading beer ingredient and the logo shape as a stop signal, plus the colour tells the user 'stop, beer here have a look'.
   
   2. The carousel slices helps as well with these inviting and warm background colours and originals stamps on the can beers.

2. As a first-time visitor, I want to be able to see what the website can offer me.

   1. The website contains ??? products, divided into categories, straightforward to reach with the button 'shop all' and the navigation bar on the header, where a bright RED?? hover colour gets the user attention to choose the category needs and navigate with one click.

3. As a first time visitor, I want to be able to get a quick and accurate research of a specific product or a specific type of beer.


   1. The website has been developed with back-end codes that take care of this specific function. All products can be found by:
   * name
   * description
   * beer taste ( citrus, fruity, tropical)
   * beer style ( lager, pale ale, ipa, stout)

   There is only one exception; the glasses obviously can not be found with the beer taste and the beer style criteria.

2. The research bar is the area where to explicate this function. Situated below the navigation bar is accessible by clicking on the search icon, and an interactive input will appear for research.

#### Returning visitor goals

1. As a returning visitor, I want to create a private account.

   1.The functionality is explicable through the  user-icon, part of the navigation bar when clicked a drop-down menu will appear with the option to register as a new user.

2. As a returning visitor, I want to see the website more interesting and more inviting.

   1. The developer will consistently monitor and update the website with new products to increase the choice to pick up different products, creating curiosity and making the user come back often to discover new items.

### Frequent user goals

1. As a frequent user, I want to be able to see my orders.

   1. The area to see the user orders is My Profile. This area consists of 2 sections. The first one displays the default delivery information, and the second one has a beneficial order history. In this way, the user can control the orders and the amount of money spent.

2. As a frequent user, I want to be able to see and read products review.

   1. The review functionality is present inside the product details template below any single product. The review can be left only from users that have an account and is made with the possibility to leave a comment and rating.

### Validator Testing


### Manual Testing

#### Search Bar

##### Expected

1. I was expected to get the research by name product, description, style product, taste product and also get the "error" meesage if any research match the query.

##### Results

1. As a result, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380253/4th%20milestone/Testing/Search%20Bar/res-console.cloudinary_a0zjel.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380187/4th%20milestone/Testing/Search%20Bar/searc-bar-test-name-check_vh9cu4.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380187/4th%20milestone/Testing/Search%20Bar/search-bar-error_fgg8ca.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380187/4th%20milestone/Testing/Search%20Bar/search-bar-test-taste_mxay3v.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380187/4th%20milestone/Testing/Search%20Bar/searc-bar-test-style-check_tghvk4.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380186/4th%20milestone/Testing/Search%20Bar/search-bar-error-message_klih1d.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380186/4th%20milestone/Testing/Search%20Bar/search-bar-test-style_qqbzj1.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380186/4th%20milestone/Testing/Search%20Bar/searc-bar-test-taste-check_ual8oc.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380177/4th%20milestone/Testing/Search%20Bar/search-bar-test-name_lfq31s.jpg)

#### Product detail quantity

##### Expected

1. I was expected to get the right quantity with the right price after clicked 'add to basket' on the pop up card on the right of the screen. So the price changes according to the quantity.

##### Results

1.As a result, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638381976/4th%20milestone/Testing/Product%20detail/quantity-function_jjxmxe.jpg)

#### My Profile

##### Expected

1. I was expected to see my delivery information, update my delivery information and my order history.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380311/4th%20milestone/Testing/My%20Profile/my-profile-order-history-info-message_ncyeud.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380310/4th%20milestone/Testing/My%20Profile/my-profile-information-update_yv1qxz.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380310/4th%20milestone/Testing/My%20Profile/my-profile-information_g1yaee.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380310/4th%20milestone/Testing/My%20Profile/my-profile-order-history_rylnli.jpg)

#### Login

##### Expected

1. I was expected to see the success toast message after login with the user name displayed.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380338/4th%20milestone/Testing/Login/login-message_obkseb.jpg)

#### Logout

##### Expected

1. I was expected to see the success toast message after login.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380498/4th%20milestone/Testing/Logout/logout-message_i2gzrx.jpg)

#### Register

##### Expected

1. I was expected, after submit the sign up form to see: the verify email message, the register email template,the confirm email with the button and the register confirmation message.

##### Results

1.  As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380526/4th%20milestone/Testing/Register/register-email-confirmation_ue2yqk.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380526/4th%20milestone/Testing/Register/register-email_u4nezs.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380526/4th%20milestone/Testing/Register/register-form_vgbctv.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380526/4th%20milestone/Testing/Register/register-email-confirmation-message_j4asci.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380525/4th%20milestone/Testing/Register/register-verify_o8heqj.jpg)

#### Basket

##### Expected

1. I was expected to see matching the quantity with the gross price and the grand total. To see the quantity, gross and the grand total price changed when the product been update with the relative message and the functionalities of the remove button and the delivery cost message. For this one, a red message when the amount is under 50£ and not message when the amount is equal or above 50£. 

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380553/4th%20milestone/Testing/Basket/basket_zn5ywf.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380553/4th%20milestone/Testing/Basket/basket-update_fg6k2a.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380553/4th%20milestone/Testing/Basket/basket-remove-message_syfee5.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380552/4th%20milestone/Testing/Basket/basket-update-grand-totaljpg_gkolwi.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380552/4th%20milestone/Testing/Basket/basket-update-price_mx6oah.jpg)

#### Checkout

##### Expected

1. I was expected to see my delivery information and  update them.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380655/4th%20milestone/Testing/Checkout/my-profile-information-update_kie38q.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380596/4th%20milestone/Testing/Checkout/checkout-save-delivery-information_hutlmd.jpg)

#### Stripe

##### Expected

1. I was expected to see the payment succeeded and the webhook events works. 

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380718/4th%20milestone/Testing/Stripe/webhook-test-events_axiqqu.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380679/4th%20milestone/Testing/Stripe/stripe-spin_rq037x.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380679/4th%20milestone/Testing/Stripe/stripe-payment-succeeded_qvxizf.jpg)

#### Product Management

##### Expected

1. I was expected to achieve all CRUD functionalities in this section.

##### Results

1.  As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380905/4th%20milestone/Testing/Product%20Management/product-management-edit-product-message_oxpqcm.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-edit-product-success_kccsna.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-edit-product_dwpqgd.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-add-product_fdc1nt.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-add-product-success_zqocuk.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-delete-product_izjyfr.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638380904/4th%20milestone/Testing/Product%20Management/product-management-add-product-price-wrong_tbt4uk.jpg)

#### Review

##### Expected

1.  I was expected to send the review post to the admin panel and display the review below the product to be visible for all users.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638881377/4th%20milestone/Testing/Review/review_a6txhd.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638881377/4th%20milestone/Testing/Review/review-admin-panel-1_koqwc2.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638881375/4th%20milestone/Testing/Review/review-admin-panel-2_nufgms.jpg)

#### Product Suggestion

##### Expected

1. I was expected to send the product suggestion post to the admin panel with the purpose to get information from the users.

##### Results

1. As a results, I achieved all functionalities that I was expected.

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638881706/4th%20milestone/Testing/Suggestion/product-suggestion-1_oaucs3.jpg)

* [View here](https://res.cloudinary.com/anto8913/image/upload/v1638881706/4th%20milestone/Testing/Suggestion/product-suggestion-2_qa85nv.jpg)

### Known Bugs

1. 

## Deployment

### Heroku Deployment

To deploy Family Hub to heroku, take the following steps:


1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key  
 --- 
AWS_ACCESS_KEY_ID 
AWS_SECRET_ACCESS_KEY
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
USE_AWS

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the main branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

### Forking the Github Repositery

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/antoniotorone?tab=repositories)

2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

3. You should now have a copy of the original repository in your GitHub account.

## Credits

### Code

[Bootstrap5.0:](https://getbootstrap.com/)

The navigation bar, the dropdown menu, buttons, grid-style, and a good quantity of class were taken from here 

[Fontawesome:](https://fontawesome.com/)

The icons were taken form here

### Content

The can and cases beer name, description, price and taste were taken from the website [honestbrew](https://honestbrew.co.uk/)

The kegs name, description, price and taste were taken fron the website [drink station](https://www.drinkstation.co.uk/)

The glasses name, description and price were taken from the website [hopt](https://www.hopt.it/)

### Media

#### All image used in this project are only for study purpose.

All can and cases beer image were taken from the website [honestbrew](https://honestbrew.co.uk/)

All kegs image were taken from the website [drink station](https://www.drinkstation.co.uk/)

All glasses image were taken from the website [hopt](https://www.hopt.it/)

## Acknowledgements 

Tutor support from CodeInstitue was critically essential. 








