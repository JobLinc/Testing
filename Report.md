# Backend

- “Email does not match user email” when registering a new user and reaching the verification screen. Fixed Quickly. Reason: Email lowercased on login but not in the verification screen.

# Cross-Platform

- There was an error in the Alerts tab and the Alerts showed 99+

## Homepage - Post, Feed, Saved Posts, Comments, Reactions, Reposts, Report
- Leaving a comment on a post with no comments deletes the comment from the "Add a comment box..." then the comment doesn't appear until you close the comment section and reopen it.
- Can comment a single space character
- Can't reply to a comment.
- Can't remove reaction from comment.
- Can't delete comment 
- Can't report comment
- Can leave reaction on post but can't remove it.
- Allows me to save post that was already saved, which gives a toast saying "Exception: internal Server error"
- Can report a post multiple times which gives a toast saying "Exception: internal Server error"
- Can't tag user in post.
- When clicking the @ sign in the beginning of the post text to start tagging, then typing anything and removing it the tag menu appears. On deleting the tag sign the tag windows continues to stay and if the post is a bit longer this obstructs the view to the post.
- The Tagging in post doesn't filter
- On making the post connections only, and clicking post, it displays a success toast. But while loading it shows "Anyone" instead of "Connections only".
- Connections can't see the connections only posts when entering the connection's profile.
- Can't attach media to post.
### What will be automated in Homepage:
- Add post
- Repost
- Report
- Saving Post
- Block User
- Make comment 
- React to comment

## Sidebar

### User Profile

### View my connections
#### What will be automated?
- View Connections 
- Remove Connection

### Saved Posts
#### What will be automated?
- Unsave post

### Reactivate Premium: 50% off
#### What will be automated?
- Pay

### Settings
- Account visibility sometimes appears to be not set even though success message appeared
#### What will be automated?
- Account Visibility

- Change Password
- Change Email Addresses
- Change Username
- Logout 
  
## Jobs
### What will be tested:
- Viewing a job
- Saving a job
- Seeing applicants on your job
- Apply to a job


### My Jobs
- Saved
- Applied
- Created
- Job Applications

### Post a Free Job
#### What will be tested:
- Creating a job 


## User Profile
- Add Experience does not work "Null" error screen



### What will be tested:
- Edit Intro
- Add Skills
- Add Licenses & Certifications
- Add Resume
- Add Education
- View Blocked List and unblock user
- Show followers list
- Show following list
- Messaging requests