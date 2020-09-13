# Testing
Back to the [README](https://github.com/ChiefChingu/reviewsfromkids/blob/master/README.md).

First I tested the project with the validators for css, markup, JS and Python. Then I manually tested all user stories and features (if relevant). All results are displayed below.

## W3C CSS Validation Service
Validator on [https://jigsaw.w3.org/css-validator/validator](https://jigsaw.w3.org/css-validator/validator) gave no errors.

Note: Bootstrap CSS has not been validated.

## W3C Markup Validation Service
Validator on [https://validator.w3.org/nu/](https://validator.w3.org/nu/) gave no errors.

## JSHint
Only one remark: undefined variable in the file "PostLoad.js". This relates to the $ sign of jQuery code and is therefore ignored.

## Pep8
If you run the code through a PEP8 checker, you will see E501 warnings: line too long.

Conform the instructions on the [offical Django site](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) I left these in and only wrapped the code to respect the limit of 119 characters.

"An exception to PEP 8 is our rules on line lengths. Don’t limit lines of code to 79 characters if it means the code looks significantly uglier or is harder to read. We allow up to 119 characters as this is the width of GitHub code review; anything longer requires horizontal scrolling which makes review more difficult. This check is included when you run flake8. Documentation, comments, and docstrings should be wrapped at 79 characters, even though PEP 8 suggests 72."

## User stories
Each user story is tested thoroughly. All steps are taken in the main browsers at 3 different viewports: mobile (including tablet) and desktop.
Some user stories have variations based on the completeness of the profile. Profile completeness levels:

- Lvl-0: user has created an account and with that a userprofile. No information except the username.
- Lvl-1: all of lvl-0 + user has filled in first name, last name, date of birth and gender.
- Lvl-2: all of lvl-1 + user has either selected hobbies or sports.
- Lvl-3: all of lvl-2 + user has both selected hobbies and sports.

### User story 1. Quickly see if a book has potential
Assume that you are a boy, age 10 and looking for a book to read. You have no account.

- Go to reviewsfromkids.herokuapp.com.
- You see two rows of books (or two grids if on non-mobile screen).
- Based on the title or front cover you decide to select a book.
- On mobile you tap and on non-mobile you hover.
- A reveal panel pops into view.
- Check the information on this panel:
    - View the rating (if any).
    - View the recommended age (if known).
    - View most liked by (if known).
    - View the category and tags.
- Based on the information in the reveal panel: quickly decide if the book can be interesting for you.
- If so, continue to user story 2.
- If not, go to the next book.


### User story 2. View individual book details.
Continuing from user story 1:

- Click on the view button.
- Detail page of the book loads:
    - Title
    - Image of front cover
    - A horizontal scrollable menu on mobile screens. A horizontal menu on tablet, laptop and larger screens.

#### For you?
This section shows:
- The average rating, if any, for this book.
- Accordeon with three main areas:
    - Kids who like this book:
        - Most liked by: calculates the gender mode of all positive ratings for this book. If no ratings: most liked by is not known yet. If no mode possible (for example 20 ratings from girls and 20 ratings from boys): most liked by all, this must be really good!
        - Recommended age: calculates the age mode of all positive ratings for this book. If no ratings: recommended age is not known yet. If no mode possible (for example 20 ratings from 10 year old and 20 ratings from 11 year old): recommended age is not available.
        - Hobbies: name of hobbies and number of kids with these hobbies.
        - Sports: name of sports and number of kids with these sports.
    - Kids who do not like this book:
        - Most disliked by: calculates the gender mode of all negative ratings for this book. If no ratings: most liked by is not known yet. If no mode possible (for example 20 ratings from girls and 20 ratings from boys): most disliked by all, this must be really bad!
        - Recommended age: calculates the age mode of all negative ratings for this book. If no ratings: recommended age is not known yet. If no mode possible (for example 20 ratings from 10 year old and 20 ratings from 11 year old): recommended age is not available.
        - Hobbies: name of hobbies and number of kids with these hobbies.
        - Sports: name of sports and number of kids with these sports.
    - Do you want to read this book?
        - If logged in: shows a heart. If put on your list, the heart is yellow. If not, the heart is grey.
        - If not logged in: message to log in if you want to add it to your list.

##### Description
- Description of the book
- Category label (clickable, starts search)
- Tag label (clickable, starts search)

##### Rating
###### Anonymous user
Message to log in or create an account.

###### Logged in user lvl-0, lvl-1, lvl-2
- Message to explain that the profile is not yet complete. 
- Link to profile page to complete profile.

###### Logged in user lvl-3
- If not rated: empty stars and a button to rate.
- If rated: your rating and an edit button to change your rating if necessary/wanted. 
- If rated: your rating and a delete link.

##### Info
Regular book info:
- Author
- ISBN
- Number of pages
- Age on book (according to publisher)


### User story 3. Search a book
There are two main flows to search for a book. The main flow, and the flow the site owner heavily promotes, is the so called book finder. The secundary flow is via the search option on the all books page. A third way to search is by clicking on the labels for category and tags.

Assume you are still the boy, 10 years old without an account. You went through user stories 1 and 2 and cannot really find interesting books.
On the home page:

#### Anonymous user
- You read the message "Find your next favorite book."
- Below this text is a button "start:.
- Click this button.
- You see the page book_finder:
    - Hero with welcome message.
    - Explanation of the book finder.
    - Call to action to start completing your profile.
    - If account: request to sign in.
    - If no account: call to action links to sign up page.
- Click the button 'Go'.

This loads the sign up page. Go to [user story 4](#user-story-4) to sign up for an account. When complete, continue the user story as logged in user.

#### Logged in user lvl-0
- You read the message "Find your next favorite book."
- Below this text is a button "start:.
- Click this button.

##### book_finder_user
- You see the page book_finder_user:
    - Hero with welcome message, this time addressing you by your username (Mr or Mrs <username>).
    - Hero has progress indicator for steps of book finder: step 0/3.
    - Explanation of the book finder.
    - Call to action to start completing your profile.
    - Back button.
- Click the button 'Sure'.

##### book_finder_user_1
- You see the page book_finder_user_1:
    - Hero with welcome message tailored to user's username.
    - Hero has progress indicator for steps of book finder: step 1/3.
    - Form with fields for first name, last name, gender and date of birth.
    - Next button to go to step 2.
    - Back button to go to step 0.
- Enter details. Make sure you choose "boy" at gender and "2010-01-01" at date of birth.
- All fields are mandatory. Try to click next without all fields completed. You see warning messages that you have to complete a field. You cannot proceed until all fields are completed.
- Complete all fields and click "next".

##### book_finder_user_2
- You see the page book_finder_user_2:
    - Hero with welcome message now tailored to user first name, gender and age.
    - Hero has progress indicator for steps of book finder: step 2/3.
    - Form with checkboxes for hobbies.
    - Next button to go to step 3.
    - Back button to go to step 1.
- Select the following hobbies: [vastleggen welke ze moeten kiezen].
- Click "next".

##### book_finder_user_3
- You see the page book_finder_user_3:
    - Hero with welcome message now tailored to user first name, gender and age.
    - Hero has progress indicator for steps of book finder: step 3/3.
    - Form with checkboxes for sports.
    - Finish button to go to results.
    - Back button to go to step 2.
- Select the following sports: [vastleggen welke sports].
- Click "finish".

##### book_finder_user_4
- You see the pahe book_finder_user_4:
    - Hero with welcome message (now tailored to user first name, gender and age).
    - Recommendations based on age, gender, hobbies and sports.
    - Link to adjust hobbies and sports (book_finder_user_5).
    - Link all books page.
    - Books are presented in table row form.
    - Every book shows:
        - Image of front cover.
        - Heart icon to indicate if this book is on your want to read list. Yellow = on list, grey = not on list.
        - Author.
        - Title.
        - Rating: average rating of a book in half stars. Ranging from zero to five.
        - Rating: number of ratings given.
        - Recommended age: calculates the age mode of all ratings for this book. If no ratings: recommended age is not known yet. If no mode possible (for example 20 ratings from 10 year old and 20 ratings from 11 year old): recommended age is not available.
        - Most liked by: calculates the gender mode of all ratings for this book. If no ratings: most liked by is not known yet. If no mode possible (for example 20 ratings from girls and 20 ratings from boys): most liked by all, this must be really good!
        - Category label: shows the main category for this book.
        - Tags label: shows further categorization for this book.

- Click on some books to go to the detail page.
- Verify that the age, gender, hobbies and sports are in accordance with your profile.

#### Logged in user lvl-3
- Restart the book finder: notice that the call to action has changed for you.
- Also notice that you go directly to the end results page (book_finder_user_4).
- Go to the bottom of the page and click the link to adjust your hobbies and sports.
- Remove [naam hobby] and click on the "take me back" button.
- Notice that the recommended books changed.

#### Concluding user story 3. Search a book
Above steps lead to books that are recommended based on your profile. At the bottom of the results page there is a link to view all books yourself (no recommendations).
In case the book finder has no results, the message will be to search yourself via all books.

This is the secundary way of searching.
- Go to all books (either via the navigation or the link at the bottom of the book finder results).
- On mobile: 
    - Click the search button.
    - See the search panel opening up.
- On desktop:
    - Search panel is visible in the left column.
- Enter the search term "Harry" in the title input field.
- Click search.
- See three search results for the term "Harry".

This is the third way of searching via labels:
- Click on category and tag labels
- Labels for category and tags are clickable and start a search. Labels that are displayed on the so-called 'sliders' (when hovering over a book card or clicking on a book card) are not clickable on purpose (otherwise it distracts/takes you out of a flow).
- When a clickable label search is started, the results are displayed on the all books page.

### User story 4. Easily register for an account
A user can register an account via the navigation > register.
A user can also get here via one of the other, indirect routes: 
- Via the book finder: login/account is required.
- Via the book detail page: for a rating, an login/account is required.
- Via the book detail page: for using the want to read list, an login/account is required.

The signup flow is:
- Sign up form with validation on email address (does it exist already), username (does it exist already) and password (has to be complex, cannot be too similar to username or email address).
    - Field completed validation:
        - Try to submit the form without email address. You will see a warning to complete the field.
        - Try to submit the form without second email address. You will see a warning to complete the field.
        - Try to submit the form without username. You will see a warning to complete the field.
        - Try to submit the form without password. You will see a warning to complete the field.
        - Try to submit the form without a second password. You will see a warning to complete the field.
    - Email format validation:
        - Try to submit a form with an invalid email address. You will see a warning to enter a valid email address.
    - Password security validation:
        - Try to submit a form with a password that is the same as your email address. You will see a warning that the password is too similar to the email address.
        - Try to submit a form with a password that is 12345678. You will see a warning that the password is too common and entirely numeric.
        - Try to submit a form with a password that is 1234. You will see a warning that the password is too short. It needs at least 8 characters (in addition it also gets the warning that it is too common and entirely numeric).
    - Repeat information validation:
        - Try to submit a form with two different, but valid email addresses. You will see a warning to enter the same email address each time.
        - Try to submit a form with two different, but valid passwords. You will see a warning to enter the same password each time.
    - Existing username validation:
        - Try to submit a form with username "sangho". You will see a warning that a user with that username already exists.
     - Existing email validation:
        - Try to submit a form with email address "book1@1.com". You will see a warning that a user is already registered with this e-mail address.

- Sign up by completing the form.
- You see a confirmation of successful signup with a message that an email is sent with a confirmation link.
- Also a notification message stays in view to make sure you check your spam. Also, your email address is shown for reference in this notification.
- Check your mail and find the mentioned email.
- Use the link from the email.
- You see an email confirmation page with your email address and username. Click the button to confirm your email address.
- You see the login page and a short notification that the email address was confirmed.
- Log in to check your account.


### User story 5. Easily log in or out
#### Log in
A user can log in via the navigation > login.
A user can also get here via one of the other, indirect routes: 
- Via the book finder: login/account is required.
- Via the book detail page: for a rating, an login/account is required.
- Via the book detail page: for using the want to read list, an login/account is required.

The usual validation applies:
- Try to login with a fake username or email address and password. You will see a warning that the username and/or password you specified are not correct.

Now log in with your correct username/password.
- You will see a notification that you are successfully logged in as "your username".
- You will see the navigation change:
    - On mobile devices: open the navigation and see that your username is visible.
    - On non-mobile devices: at the to right you see your username.

#### Log out
- On mobile devices: open the navigation and click logout.
- On non-mobile devices: hover over your profile name. Click on logout.
- You see a logout page with a sign out button.
- Click the button.
- You see the homepage with a notification that you have signed out.


### User story 6. Easily recover my password if necessary
- Go to the login page.
- Click the link 'forgot password'.
- You see a password reset request form.
- Enter the email address of your account and submit.
    - Note that there is email validation:
        - Try to add an incorrect email address format. You will see a warning to enter a valid email address.
        - Try to add a non-existent email address. You will see a warning that the email address is not assigned to any user account.
- You see a confirmation page explaining that you have an email with instructions.
- Go to your inbox and find the email.
- Click on the link.
- You see a password reset form.
- This form has the same validation as the register form:
    - Try to submit a form with a password that is the same as your email address. You will see a warning that the password is too similar to the email address.
    - Try to submit a form with a password that is 12345678. You will see a warning that the password is too common and entirely numeric.
    - Try to submit a form with a password that is 1234. You will see a warning that the password is too short. It needs at least 8 characters (in addition it also gets the warning that it is too common and entirely numeric).
- Enter a new, valid password.
- You see a confirmation page and a notification that your password is successfully changed.
- Click the login button.
- Log in with your changed password.


### User story 7. Have a personalized user profile.
Upon account creation, an empty userprofile is created. User can update this profile in two ways.

The main mechanism is the book finder. The secundary flow is directly in 'my profile'.

For book finder see [Logged in user lvl-0](#logged-in-user-lvl-0).

The 'my profile' flow:
- On mobile devices open the navigation and click on my profile.
- On non-mobile devices hover over your username and select my profile.
- You see your profile page.
- The hero shows a message based on your profile completeness level:
    - lvl-0: hello anonymous, profile at 0%.
    - lvl-1: hello first name, profile at 50%.
    - lvl-2: hello first name, profile at 75%.
    - lvl-3: hello first name, profile at 100%.
- The page has a horizontally scroll nav on mobile. On all other devices (tablet, laptop and larger) it is a horizontal nav without scroll.
- The nav contains "Account", "Hobby & Sport", "Ratings" and "Want to read".

##### Account
- Shows Account info: username and email.
    - Edit button opens a modal. You can send an email to site owner if you need to change your email or username.
- Shows Personal info: first name, last name, date of birth and gender.
    - If not completed (lvl-0) a CTA shows to complete.
    - Edit button opens edit personal page.
    - If present, existing data is pre-filled.
    - When saving edit form, message confirms your changes are saved.

##### Hobby & Sport
- If not completed: shows CTA to complete.
- If filled out, shows your hobby and sport.
- Also shows an edit button to change.
    - Edit hobby/sport:
        - Explanation/instruction.
        - Call to action to contact site owner if there is a hobby/sport not in the list.
        - Form with checkboxes for hobbies/sports.
        - Save button to save changes and go back to hobby/sport overview.
    - When saving edit form, message confirms your changes are saved.

##### Ratings
- If not lvl-3: CTA to complete profile.
- If lvl-3 and no ratings: "You have not rated any books yet."
- If lvl-3 and ratings:
    - If positive rating (4 or 5 stars): all books with your positive rating.
    - If neutral rating (3 stars): all books with your neutral rating.
    - If negative rating (1 and 2 stars): all books with your negative rating.
- Books are displayed in table row format. Similar to [All books page](#all-books-page).

##### Want to read
- If no books on list, teaser to add books.
- If books on list, books are displayed in table row format. Similar to [All books page](#all-books-page).
- All books have a yellow heart.


### User story 8. Keep a list of books I want to read.
#### Anonymous user
- Log out.
- Go to a book via the homepage, book finder or all books.
- Click on "Do you want to read this book?"
- View the message: "Please log in to add to your list".

#### Logged in user
- Log in or create an account.
- Go to a book via the homepage, book finder or all books.
- Click on "Do you want to read this book?"
- Click on the heart to add the book to your list.
- View the notification that the book is on your list. Also, see that "Do you want to read this book?" has changed to "This book is on your list".
- Click on "This book is on your list".
- See that the heart is yellow and the text says that this book is on your list.
- Go to your profile.
- Click on want to read.
- You see the book that you just added.
- Go to all books.
- Look for the book you just added.
- See that the little heart is now yellow.


### User story 9. Leave a rating for a book.
#### Anonymous user
- Log out.
- Go to a book via the homepage, book finder or all books.
- Click on "Your rating" in the horizontal navigation.
- View the message: "We love your rating please log in".

##### Logged in user lvl-0, lvl-1, lvl-2
- Log in or create an account.
- Go to a book via the homepage, book finder or all books.
- Click on "Your rating" in the horizontal navigation.
- View the message: "Please complete your profile here."
- Follow the link to the profile page to complete your profile.

##### Logged in user lvl-3
- Log in and go to a book you want to rate.
- Click on "Your rating" in the horizontal navigation.
- If not rated: empty stars and a button to rate. After rating, confirmation notification with your rating: "rated with a x".
- If rated: your rating and an edit button to change your rating if necessary/wanted. After editing: confirmation message "rating changed to x".
- If rated: your rating and a delete link. After deleting: confirmation message "rating deleted".


### User story 10. Get personalized recommendations
This user story is covered by [User story 3. Search a book](#user-story-3.-search-a-book). 


### User story 11. Make a donation
- Go to the donations page via the navigation. On mobile open the menu and click 'donations'.
- View the donations page and see four options:
    - On mobile: horizontal scroll box with one option in full view. The second option is partially visible, giving a visual cue that you can scroll.
    - On tablet: horizontal scroll box with two options in full view. The third option is partially visible, giving a visual cue that you can scroll.
    - On laptop and larger screens: grid with 2x2 options.
- Pick an option and click 'checkout'.
- Complete the form with this card information:
    - Email: 1@1.com.
    - Card number: see below.
    - MM/YY: 04/24.
    - CVC: 424.
    - Name on card: name.
- Try to enter the following card numbers:
    - 4000000000000002 (error message: card is declined).
    - 4000000000009995 (error message: insufficient funds).
    - 4000000000000069 (error message: expired card).
    - 4000000000000127 (error message: incorrect cvc).

- Now use card number: 4242 4242 4242 4242.
- Click the 'pay' button.
- View the success page on reviewsfromkids.herokuapp.com.


### User story 12. Send a message to the site owner
- Go to the contact page via the footer.
- Try to submit the form without completing all fields.
    - You see validation messages on all fields.
- Complete the form and send.
- You see the contact page reload with empty fields.
- You see a success message that stays on screen until you close it or navigate away.

## Features
Most of the features are covered by the test of user stories. Remaining features are tested individually and work as intended.