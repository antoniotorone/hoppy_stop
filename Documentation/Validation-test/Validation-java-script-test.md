# Java Script Validator

## Stripe.js

* The test came out with two undefined variables regarding $ and two warnings that says 'template literal syntax' is only available in ES6 (use 'esversion: 6'). For the undefined variables, I'm aware to use jquery, the jquery method does not damage the web functionality and this is why I left untouched.Regarding the two warnings I added on the top of the validator on line 1, a comment "/*jshint esversion: 6 */ that delete all these type of warnings.[View the test](https://github.com/antoniotorone/hoppy_stop/blob/main/Documentation/All-validation-test-PDF/stripe.pdf)


## Script.js

* For script.js the test came out with two undefined variables and five warnings, the same of stripe.js. I'm aware to use jquery in this file as well and for the five warnings I used the same method described above.[View the test](https://github.com/antoniotorone/hoppy_stop/blob/main/Documentation/All-validation-test-PDF/script.pdf)