[Introduction](#introduction)

[UX](#ux)

[Features](#features)

[Data structure](#data-structure)

[Technologies used](#technologies-used)

[Testing](#testing)

[Clone & Deploy](#clone-&-deploy)

[Credits](#credits)

[Remark for assessment](#remark-for-assessment)

## Introduction
This is the fourth and final milestone project of the fullstack software development course of Code Institute. Covid-19 forced a lockdown in the Netherlands. This brought to light the need for things to do for our kids. One of the easy things is to allow more screen time (games, youtube, TV). Better though, is when they read more books. This led to a problem that my son did not know what to read. I tried to find some suggestions, but these were very general in nature and not at all specific for my kid. I looked for a review site where other kids would recommend books, but there were none!

That is why I decided to start reviewsfromkids.com. A site where kids recommend the books they like. To make the reviews as relevant as possible I combine these with profile information. This means for instance that if you are a girl with age 10 you get to see different recommendations than a boy with age 8. Because of the time constraints (hard deadline to graduate before August 31st), I omitted recommendations based on favorite music and movies.

The live project can be found here: [https://reviewsfromkids.herokuapp.com](https://reviewsfromkids.herokuapp.com).

## UX
All designs start from the mobile perspective. Larger viewports are handled with media queries.

### Strategy Plane
#### Product objectives
As a site owner my objective is to get kids to read more by providing them with a list of books that they most likely will enjoy. 

As a student my objective is: to show my skills and qualifications in order to pass the fourth milestone project with a score of at least 80% in order to receive 'first grade honors' at the end of the complete course.

#### User needs
Main user is a user who wants to find a book. This user can be anonymous (no account and thus no profile), partly anonymous (with account and a minimum profile) and fully known (with account and a full profile). The more information a user shares, the better information he or she receives.

##### User needs main user
- Easy and intuitive way to find a book.
- Quick confirmation that a book is a match.
- Keep track of the books you want to read.

##### User needs site owner
- Easy upload of new books.
- Insight in quality of recommendations.
- Analytics on user acquisition and growth.

### Scope Plane
When designing this project a lot of ideas came up. Keeping the main objective in mind (pass the fourth milestone project before August 31st) I decided to have these main features (Full details on features: [Features](#features).)

#### Main features
- User profile with levels of completeness: lvl-0 is the basic profile with username only; lvl-3 is the full profile with name, gender, age, hobbies and sports.
- Book finder: flow to complete the user profile and get recommendations for books.
- Star rating system: rate books with 1 to 5 stars.
- Most liked by: based on ratings show whether the book is recommened most by boys or girls.
- Recommended age: based on ratings show the most frequent age of users that rated the book.

### Structure Plane
The structure of the site is straightforward: a homepage connects to the books overview page, the bookfinder, the donations page and the usual pages for about, contact, registration, login, privacy and cookies. When logged in, the homepage also connects to the profile page.

- The books overview has the book details as children.
- The profile page has the edit profile sections as children.
- The bookfinder has several steps as children (depending on what lvl your profile is. If lvl-0 then all steps are triggered. If lvl-3 you skip to the end result directly)

Schematically, this looks as follows:

![structure-plane](https://github.com/ChiefChingu/reviewsfromkids/blob/master/structure-plane.png)

In Django terms this structure resulted in four apps:

1. Books
2. Donations
3. Home
4. Profiles

At first there was a fith app 'Ratings'. However, while developing it soon became clear that it was more efficient to integrate this into the Books app.


### Skeleton Plane
This project is designed with the mobile user in mind: mobile first and desktop second. The mobile viewport is the baseline. Media queries are used to handle the larger viewports.

The wireframes are found [here](https://github.com/ChiefChingu/reviewsfromkids/blob/master/wireframes%20reviewsfromkids.pdf). 

### Surface Plane
The final product can be viewed [here](https://reviewsfromkids.herokuapp.com).

#### Typography
For this project a combination of the Google font Quicksand and Open Sans is used. Quicksand is used for headers and Open Sans for all other content. This provides an appearance that is open, neutral and friendly.

#### Color palette
The background color is white for two reasons. The first is that it is easy on the eye and provides a clean and clear background. This makes it possible to add accents with rather contrasting colors:

- The header and mobile nav are purple (#7d51a1).
- The hero section of the page groups:
    - Home, account creation/log in and book finder: light blue (#52c5fb), 
    - Contact, about: dark blue (#2a97ce),
    - Profile: teal (#25b8c0).
- Call to action: orange (#ff8d1a).
- Emphasis: pink (#e166c4).
- Hover links: yellow (#fec944).

The contrasting colors are checked in a [color blind web page filter](https://www.toptal.com/designers/colorfilter) with good results on all filters.

The second reason for a white background is that children's books tend to have fairly colorful and contrast-rich front covers. With a largely white background these colorful images do not get to chaotic on the eye.


### User Stories
There are two distinct roles: the main user and the site owner. The main user has some authorisation levels:
- Anonymous (lvl-0): can only view, cannot interact (rate, add to list, start book finder), cannot get tailored recommendations.
- Basic account (lvl-1 and lvl-2): can view and start book finder and add to list (cannot rate), can get some recommendations based on profile completeness.
- Full account (lvl-3): can view and interact, can get the best recommendations.

#### As a user I want to be able to
1. Quickly see if a book has potential.
2. View individual book details.
3. Search a book by meaningful criteria.
4. Easily register for an account.
5. Easily log in or out.
6. Easily recover my password if necessary.
7. Have a personalized user profile.
8. Keep a list of books I want to read.
9. Leave a rating for a book.
10. Get personalized recommendations.
11. Make a donation.
12. Send a message to the site owner.

#### As a site owner I want to be able to
1. Easily upload new books.
2. Easily promote new books.


### Defensive design
The site has been designed defensively, gating content and functionality. This is done by:
- using the ```@login required``` functionality in the views.py. A user cannot access the view without being logged in. He/she is redirected to the login page when trying to access the view.
- hiding buttons via template logic with statements like ```if user_logged_in```, based on ```if user.is_authenticated```.
- restricting by profile levels: logged in users without the right profile level cannot rate.

## Features
### Existing features
#### Site wide
- Clickable logo leading to the homepage.
- Hamburger menu that opens a modal for navigation.
- For larger viewports: navigation is shown in the header.
- Navigation linking to all pages.
- In case of a logged in user: the modal shows the logged in user name.
- On large screens: in case of a logged in user: hover over the user name shows a link to the profile page and the logout page.
- Footer with links to contact, about, privacy policy, cookie policy and social accounts.
- Profile completeness levels:
    - Lvl-0: user has created an account and with that a userprofile. No information except the username.
    - Lvl-1: all of lvl-0 + user has filled in first name, last name, date of birth and gender.
    - Lvl-2: all of lvl-1 + user has either selected hobbies or sports.
    - Lvl-3: all of lvl-2 + user has both selected hobbies and sports.

#### Home page
##### All users
- Hero box with call to action.
- Featured books: books that site owner wants to promote.
- Recently added books: books that are recently added.
- Both featured and recently added: 
    - On mobile: horizontal slider with books.
    - On larger screens: grid layout with books.
    - Books are in card form showing the front cover.
    - On mobile: tap on book activates 'slider' content with:
        - Rating
        - Recommended age
        - Most liked by
        - Category label
        - Tag labels
    - On desktop this 'slider' is activated by mouse hover.
- How it works section to explain how the site works.
- Call to action.

###### Anonymous users and lvl-0, lvl-1 and lvl-2 users
- Call to action in hero is to find your next favorite book.
- Call to action at bottom is to join.
- Both calls to action link to step 1 of book finder.

###### lvl-1 and lvl-2 users
- Call to action at bottom is now 'start'.

###### Logged in users with profile lvl-3
- Call to action in hero is to check your recommendations.
- Call to action at bottom is to start.
- Both calls to action link to results of book finder.
</details>

#### Book finder
The book finder is a tool with two objectives:
1. To complete the user profile.
2. To provide recommendations to user.

##### Anonymous users
- Book_finder:
    - Hero with welcome message.
    - Explanation of the book finder.
    - Call to action to start completing your profile.
    - If account: request to sign in.
    - If no account: call to action links to sign up page.

##### Logged in user with lvl-0
###### book_finder_user:
- Hero with welcome message tailored to user's username  and progress indicator for steps of book finder.
- Call to action to complete the profile.

###### book_finder_user_1:
- Hero with welcome message tailored to user's username  and progress indicator for steps of book finder.
- Form with fields for first name, last name, gender and date of birth.
- Next button to go to step 2.
- Back button to go to step 0.

###### book_finder_user_2:
- Hero with welcome message (now tailored to user first name, gender and age) and progress indicator for steps of book finder.
- Form with checkboxes for hobbies.
- Next button to go to step 3.
- Back button to go to step 1.

###### book_finder_user_3:
- Hero with welcome message (now tailored to user first name, gender and age) and progress indicator for steps of book finder.
- Form with checkboxes for sports.
- Finish button to go to results.
- Back button to go to step 2.

###### book_finder_user_4:
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
    - Category label: shows the main category for this book. Starts a search on click to show other books within this category.
    - Tags label: shows further categorization for this book. Starts a search on click to show other books with the same tags.

###### book_finder_user_5:
- Hero with instructions.
- Hero button to go back to results of book finder.
- Overview of the hobbies and sports that user has selected.
- Edit buttons to change the hobbies and sports. Opens book_finder_edit_hobby and book_finder_edit_sports respectively.

###### book_finder_edit_hobby:
- Explanation/instruction.
- Call to action to contact site owner if there is a hobby not in the list.
- Form with checkboxes for hobbies.
- Save button to save changes and go back to book_finder_user_5.

###### book_finder_edit_sport:
- Explanation/instruction.
- Call to action to contact site owner if there is a sport not in the list.
- Form with checkboxes for sports.
- Save button to save changes and go back to book_finder_user_5.

##### Logged in user with lvl-1
###### book_finder_user:
- Hero with welcome message (now tailored to user's first name, gender and age) and progress indicator for steps of book finder.
- Call to action to complete the profile.
- Button to go to find_user_2 (so, skip find_user_1, since this information is available).
- Back button to go back to home.

The rest of the flow is similar to that of lvl-0 users. Starting at [book_finder_user_2](#book-finder-user-2).

##### Logged in user with lvl-2
###### book_finder_user:
- Hero with welcome message (now tailored to user's first name, gender and age) and progress indicator for steps of book finder.
- Call to action to complete the profile.
- Button to go to find_user_2 (so, skip find_user_1, since this information is available).
- Back button to go back to home.

###### book_finder_user_2:
- Users with lvl-2 have either hobbies or sports filled in. Depending on which they have, the user sees a form of what they do not have completed yet.
- Hero with welcome message (now tailored to user first name, gender and age) and progress indicator for steps of book finder.
- Form with checkboxes for hobbies or sports.
- Save button to go to step 4.
- Back button to go to step 1.

See [book_finder_user_4](#book_finder_user_4) above.

##### Logged in user with lvl-3
User has completed the profile and goes to the results directly. See [book_finder_user_4](#book-finder-user-4) above.


#### All books page
The all books page shows all books. 
- On mobile screens it shows a search button at the top. On click a search panel is toggled (see [search](#search) for more details).
- On larger screens the screen is split in two columns. The left column is dedicated to search. The right column shows all books and/or the search results (see search for more details).
- Books are in a table row format. Every book shows:
    - Image of front cover.
    - Heart icon to indicate if this book is on your want to read list. Yellow = on list, grey = not on list.
    - Author.
    - Title.
    - Rating: average rating of a book in half stars. Ranging from zero to five.
    - Rating: number of ratings given.
    - Recommended age: calculates the age mode of all positive ratings for this book. If no ratings: recommended age is not known yet. If no mode possible (for example 20 ratings from 10 year old and 20 ratings from 11 year old): recommended age is not available.
    - Most liked by: calculates the gender mode of all positive ratings for this book. If no ratings: most liked by is not known yet. If no mode possible (for example 20 ratings from girls and 20 ratings from boys): most liked by all, this must be really good!
    - Category label: shows the main category for this book. Starts a search on click to show other books within this category.
    - Tags label: shows further categorization for this book. Starts a search on click to show other books with the same tags.


#### Search
Search can be initiated in different ways. You can search via the search functionality on the all books page. Or you can start a search by clicking on the category and tag labels.

##### Search panel
###### Mobile screens
- Click on the search button toggles a search panel.
- Search criteria are title, author, category, most liked by, recommended age and rating from.
- When doing a search the search panel hides and the search results are displayed.
- The number of search results are shown.
- The books of the search results are shown.
- In case there are no results, this message appears: "Your search has no success. Try again!"
- After a search, the search panel can be toggled again and your initial query is still visible. Also, a link is visible to reset your search.
- You can alter/expand your search infinitely until you do a hard refresh of the page or hit the reset search button.

###### Non-mobile screens
Same as above except for:
- Search is visible in the left column of the page.
- Search panel shows the initial query until search is reset or the page is hard refreshed.

##### Click on category and tag labels
Labels for category and tags are clickable and start a search. Labels that are displayed on the so-called 'sliders' (when hovering over a book card or clicking on a book card) are not clickable on purpose (otherwise it distracts/takes you out of a flow).

When a clickable label search is started, the results are displayed on the all books page.


#### Book detail page
Book detail page shows:
- Title
- Image of front cover
- A horizontal scrollable menu on mobile screens. A horizontal menu on tablet, laptop and larger screens.

##### For you? 
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
        - If added to list: message to confirm it is added.
        - If removed from list: message to confirm removal plus CTA to rate the book if applicable.
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
- If not rated: empty stars and a button to rate. After rating, confirmation notification with your rating: "rated with a x".
- If rated: your rating and an edit button to change your rating if necessary/wanted. After editing: confirmation message "rating changed to x".
- If rated: your rating and a delete link. After deleting: confirmation message "rating deleted".

##### Info
Regular book info:
- Author
- ISBN
- Number of pages
- Age on book (according to publisher)


#### Profile
- Only accessible for logged in users.
- Shows hero with message based on profile level.
- Shows horizontal scroll nav on mobile devices. A horizontal menu on tablet, laptop and larger screens.
- Nav contains: account, hobby & sport, ratings and want to read.

##### Hero
Shows message based on profile completeness. Shows profile % complete.

###### lvl-0
- 'Hello anonymous'
- Profile at 0%.

###### lvl-1
- 'Hello first name'
- Profile at 50%.

###### lvl-2
- 'Hello first name'
- Profile at 75%.

###### lvl-3
- 'Hello first name'
- Profile at 100%.

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


#### Donate
- Hero with teaser.
- CTA to donate if happy with site.
- Four donation choices.
- Checkout button to secure environment of Stripe.
- If donated successfully: thank you page.


#### Account pages
The django-allauth package is used for sign up and password recovery. All features are out of the box. I only added hero sections with related icons. Also, I added additional copy (explanation) and styling.

The signup flow is:
- Sign up form with validation on email address (does it exist already), username (does it exist already) and password (has to be complex, cannot be too similar to username or email address).
- Confirmation of successful signup with message that an email is sent with a confirmation link.
- When link from email is used, you land on a email confirmation page. Click a button to confirm your email address.
- Redirect to log in page to log in.

Password recovery flow:
- Click forgot password leads to password reset form.
- Enter email address and submit.
- Confirmation of password reset started. Message that an email has been sent.
- In email link to a change password form.
- On change password form: enter new password with all validations.
- When successfully submitted, a confmiration page is loaded. Also, a success notification is shown.

Log in flow:
- Log in form with remember me option.
- After successful login, redirect to homepage. Also, a success notification is shown.

Log out flow:
- Click log out in the menu.
- Log out page is loaded with confirm button.
- After successful logout, redirect to homepage. Also, a success notification is shown.


#### About page
- Hero.
- Explanation.


#### Contact page
- Hero.
- Call to action to feel free to send any inquiry.
- Contact form.
- Send button.
- When successfully submitted: success notification is shown.


#### Cookie Policy
Links to external page with cookie policy.


#### Privacy Policy
Links to external page with privacy policy.


### Features left to implement
- Show books based on profile: now only in the book finder feature. Plan is to use this 'view' as default view for all books, home page, etc. User can toggle this view on and off.
- Allow users to write a review.
- Share want to read lists.
- Pagination for all books view and book finder results.
- Several features for business models like affliate links to amazon, a merchandize webshop and promotion deals with publishers.
- Add more payment gateways.


## Database
The project uses relational databases SQLite and PostgreSQL. At the start when learning how to work with Django, I used SQLite. Once I had a basic understanding of how to work with SQL I moved to PostgresQL. I use a local Postgres database for local development. For production I use Heroku's service for Postgres called Heroku Postgres.

### Database Overview
The database overview is displayed below.

![database-overview](https://github.com/ChiefChingu/reviewsfromkids/blob/master/db-overview.png)

At the start of the project I created tables for features like the favorites list. Later it became clear that this was not necessary: lots of data points are now integrated in the book, ratings and userprofile tables.

For more details, please view the models.py files of the respective apps.


## Technologies Used
### Languages
- HTML
    - to create the elements
    - [https://whatwg.org](https://whatwg.org)
- CSS
    - to style the html elements
    - [https://www.w3.org/Style/CSS/](https://www.w3.org/Style/CSS/)
- JavaScript
    - to provide interactivity and logic
    - [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Python
    - for backend application
    - [https://www.python.org](https://www.python.org)
- Jinja
    - for templating logic
    - [https://jinja.palletsprojects.com/en/2.11.x/](https://jinja.palletsprojects.com/en/2.11.x/)

### Frameworks
- Django
    - high-level Python framework
    - [https://www.djangoproject.com/](https://www.djangoproject.com/)


#### Python/Django packages
A host of packages are used in this project. Please view the [requirements.txt](https://github.com/ChiefChingu/reviewsfromkids/blob/master/requirements.txt) to see the complete list.

### Libraries
- JQuery
    - only for the shuffle cards function (see [Credits](#credits))
    - [https://jquery.com](https://jquery.com)
- Google Fonts
    - to use Lato fonts
    - [https://fonts.google.com/specimen/Lato](https://fonts.google.com/specimen/Lato)
- Font Awesome
    - to use icons
    - [https://fontawesome.com](https://fontawesome.com)
- Bootstrap
    - to quickly add styling and interactivity
    - [https://getbootstrap.com/](https://getbootstrap.com/)

### Database
- PostgreSQL
    - relational database used for this project
    - [https://www.postgresql.org/](https://www.postgresql.org/)
- SQlite
    - relational database used at the start of this project
    - [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)

### Other tools
- SCSS
    - to write custom CSS, especially for grids
    - [https://sass-lang.com](https://sass-lang.com)
- npm
    - to install SCSS
    - [https://www.npmjs.com](https://www.npmjs.com)
- Color blind filter
    - to check the used color palette
    - [https://www.toptal.com/designers/colorfilter](https://www.toptal.com/designers/colorfilter)
- GT Metrix
    - to check the loading times
    - [https://gtmetrix.com](https://gtmetrix.com)
- JSHint
    - to check JavaScript
    - [https://jshint.com](https://jshint.com)
- Markup Validation Service
    - to check HTML
    - [https://validator.w3.org](https://validator.w3.org)
- CSS Validation Service
    - to check CSS
    - [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
- Autoprefixer CSS online
    - to add vendor prefixes
    - [https://autoprefixer.github.io](https://autoprefixer.github.io)
- Squoosh
    - tool to compress and resize images
    - [https://squoosh.app/](https://squoosh.app/)
- dbdiagram
    - tool to create database diagrams
    - [https://dbdiagram.io/](https://dbdiagram.io/)
- favicon.io
    - tool to generate favicons
    - [https://favicon.io/favicon-generator/](https://favicon.io/favicon-generator/)


## Testing
All standard online tests passed without any major problems.

The online and manual tests are detailed in the [TEST.md](https://github.com/ChiefChingu/reviewsfromkids/blob/master/TEST.md)


## Clone & Deploy
### Deploy locally
#### Cloning a repository
To run this site locally, you can clone the repository. For a detailed description how to do so, please visit [this guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

#### Create and activate a virtual environment
Once cloned on your local machine, it is highly recommended to create a virtual environment for the remainder of the setup. This virtual environment will box the Python code, which ensures that the packages of this project will not interfere with the packages of your other projects and vice versa.

Create a virtual environment to make sure dependencies only apply to this project.

Open your console.
Make sure you are in the folder of this project.
Type ```python -m venv env```.
Open the command palette (ctrl + shift + p).
Type 'Python select interpreter' and select.
Select your Python version in the dropdown (in my case 'Python 3.7.7 64-bit ('env':venv)').
Then activate your virtual environment (ctrl + shift + `).
You'll see ```(env)``` before the directory name in your terminal. This means that the virtual environment is activated.

#### Install Django and packages
Type pip3 install -r requirements.txt. This will install all necessary programs and packages.

#### Create env.py and generate secret key
To keep sensitive information out of version control and publicly accessible locations:
- Create a file in the root called env.py.
- Go to [django-secret-key-generator](https://miniwebtool.com/django-secret-key-generator/).
- Generate a secret key.
- Add a line in your env.py: SECRET_KEY = 'copy the secret key here, between the apostrophes'

#### Remove unnecessary imports from env.py
To run locally, you do not need the following statement in the settings.py (line 6):
```
if os.path.exists("env.py"):
    import env
    from env import SECRET_KEY, POSTGRES_PASS, STRIPE_API_KEY_TEST,\
        DATABASE_URL, GMAIL_KEY
```

Remove everyting except the SECRET_KEY.

#### Setup a local database
- The easiest way is to use the SQLite database that comes with Django by default.
- First go to the file settings.py (in the folder reviewsfromkids).
- Locate the following statement (line 129):

```
if 'DATABASE_URL' in os.environ:

    DATABASES = {

        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

else:

    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'reviewsfromkids',
            'USER': 'postgres',
            'PASSWORD': POSTGRES_PASS,
            'HOST': '127.0.0.1',
            'PORT': '5432',

            }
        }
```

- Replace the else branche with this code:

```
else:

    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.sqlite',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

            }
        }
```

#### Migrate and load data
To configure the database run the following commands:
- ```python manage.py makemigrations```.
- ```python manage.py migrate```.
- ```python manage.py loaddata categories```.
- ```python manage.py loaddata books```.
- ```python manage.py loaddata hobbies```.
- ```python manage.py loaddata sports```.

#### Create superuser
To create a superuser type ```python manage.py createsuperuser``` and follow the instructions.

#### Run the app locally
- Type the command ```python manage.py runserver``` and go to http://127.0.0.1:8000/
- You should see the homepage with four featured books and eight recently added books.
- Note that there is no information about ratings and recommendations.

### Deploy on Heroku with AWS S3
To deploy the web app Heroku is used in combination with AWS S3 (Simple Storage Service). S3 allows you to offload the storage of static files from your app. This is crucial on Heroku, because your app’s dynos have an ephemeral filesystem. This means that all files that aren’t part of your application’s slug are lost whenever a dyno restarts or is replaced (this happens at least once daily).

#### Replace settings.py if you did local deployment first
In order to run the app locally, the settings.py was changed (see [above](#deploy-locally)). If you followed these steps, you need to undo these changes first.

#### Heroku and AWS S3
To setup Heroku with AWS S3 you first need to create accounts.

- [Heroku](https://signup.heroku.com/login)
- [Amazon](https://aws.amazon.com/s3/#)

Then follow all steps from this execellent tutorial:
1. [Part 1 - Heroku](https://www.youtube.com/watch?v=6mv-Qp37X4I&list=PLTuxCJD6mnp5XTy0YAQIxpHaumA69AZkQ&index=77&t=0s)
2. [Part 2 - Heroku](https://www.youtube.com/watch?v=Tp2CU1qpgJo&list=PLTuxCJD6mnp5XTy0YAQIxpHaumA69AZkQ&index=77)
3. [Part 3 - S3 Bucket](https://www.youtube.com/watch?v=uGdZeX319Q4&list=PLTuxCJD6mnp5XTy0YAQIxpHaumA69AZkQ&index=78)

Code for CORS:
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

4. [Part 4 - IAM](https://www.youtube.com/watch?v=BzzjLvC0Fcc&list=PLTuxCJD6mnp5XTy0YAQIxpHaumA69AZkQ&index=79)
5. [Part 5 - Media files](https://www.youtube.com/watch?v=JPb82nILolU&list=PLTuxCJD6mnp5XTy0YAQIxpHaumA69AZkQ&index=80)

## Credits


## Remark for assessment
Due to time constraints, severely aggrevated by COVID-19 and some personal events, I was not able to implement the following:

- A server-side implementaion of Stripe. I got a rather easy one running, but then got some issues with error codes like insufficient funds. I decided to move to client-side code with a secure checkout on the Stripe domain. Some code is left in (like the keys for Heroku) for future reference.

- A context processor for want to read list. Like a checkout basket/cart you always have your want to reads available.

- Refactor code and limit repeating functions in views.
