CLICK "follow":

1. Text "follow" must change to "following" on button (JavaScript).
2. When a user clicks "follow", you execute a JS function that calls your API.
3. The API should "INSERT" into the "follow"-table (if you have created the connection between the keys it will automatically not be possible to follow yourself or another user twice)
4. If the API call goes through (Check if rowCount was altered), then make sure to return a "followed" response.
5. If the API call doesn't go through (Rowcount is 0), make sure to return an "unfollowed" response.

Last but not least; you need to update the users table column for "user_total_followers".
If RowCount was altered you increment with one
If rowcount was not altered, you decrement with one.

You get the follow_user_follower_fk from the cookie
You get the follow_user_followee_fk from the data-id attribute in the button, inside the form.

follow table in DB:
follow_user_follower_fk
follow_user_followee_fk

Must connect those two via a compound key (I think that's what it's called. It ensures you can't follow the same person twice)

Update total followers in users table
