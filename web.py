
ProfilePage 
component:
#js
# ProfilePage.jsx
'use client';
import { useState, useEffect } from 'react';

import ProfileCard from './components/ProfileCard';

import EditProfileForm from '@/app/components/EditProfileForm';

import styles from '@/app/Profile.module.css';
const ProfilePage = () => {

  const [userId, setUserId] = useState(1);

  const [displayId, setDisplayId] = useState(1);

  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState(null);

  const [isEditing, setIsEditing] = useState(false);



  // Fetch user data whenever userId changes

  useEffect(() => {

    const fetchUser = async () => {

      setLoading(true);

      setError(null);

      try {

        const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/user/${userId}`);



        if (!response.ok) {

          throw new Error(`Error: ${response.status} ${response.statusText}`);

        }



        const userData = await response.json();

        setUser(userData);

      } catch (err) {

        console.error('Failed to fetch user data:', err);

        setError(err.message);

        setUser(null);

      } finally {

        setLoading(false);

      }

    };



    fetchUser();

  }, [userId]);



  const handleSave = async (updatedUser) => {

    setLoading(true);

    setError(null);

    try {

      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/user/${displayId}`, {

        method: 'PUT',

        headers: {

          'Content-Type': 'application/json',

        },

        body: JSON.stringify(updatedUser),

      });



      if (!response.ok) {

        const errorData = await response.json();

        throw new Error(errorData.error || 'Failed to update profile');

      }



      const updatedData = await response.json();

      setUser(updatedData); // Update local user state with the latest data

      setIsEditing(false); // Exit edit mode

    } catch (err) {

      console.error('Failed to update user data:', err);

      setError(err.message);

    } finally {

      setLoading(false);

    }

  };



  const handleCancel = () => {

    setIsEditing(false); // Exit edit mode without saving

  };



  const handleUserIdChange = (e) => {

    setDisplayId(Number(e.target.value))

    setUserId(Number(e.target.value)-1);

    setIsEditing(false); // Exit edit mode if a different user is selected

  };



  return (

    <div className={styles.container}>

      <h1>User Profile</h1>



      {/* User ID Selection */}

      <div className={styles.selector}>

        <label htmlFor="userId">Select User ID:</label>

        <select id="userId" value={displayId} onChange={handleUserIdChange}>

          <option value={1}>1</option>

          <option value={2}>2</option>

          <option value={3}>3</option>

        </select>

      </div>



      {/* Loading and Error States */}

      {loading && <p>Loading user data...</p>}

      {error && <p className={styles.error}>Error: {error}</p>}



      {/* Display User Profile */}

      {user && !isEditing && (

        <ProfileCard user={user} onEdit={() => setIsEditing(true)} />

      )}



      {/* Edit Profile Form */}

      {isEditing && user && (

        <EditProfileForm user={user} onSave={handleSave} onCancel={handleCancel} />

      )}

    </div>

  );

};



export default ProfilePage;





EditProfileForm component:

js

// EditProfileForm.jsx



import { useState } from 'react';

import styles from './styles/EditProfileForm.module.css';



const EditProfileForm = ({ user, onSave, onCancel }) => {

  const [name, setName] = useState(user.name);

  const [email, setEmail] = useState(user.email);

  const [bio, setBio] = useState(user.bio);

  const [form, setForm] = useState({

    name: user.name,

    email: user.email,

    bio: user.bio,

  });



  const handleNameChange = (e) => {

    const newVal = e.target.value;

    setName(newVal);

    setForm({ ...form, name: newVal });

  };



  const handleEmailChange = (e) => {

    const newVal = e.target.value;

    setEmail(newVal);

    setForm({ ...form, email: newVal });

  };



  const handleBioChange = (e) => {

    const newVal = e.target.value;

    setBio(newVal);

    setForm({ ...form, bio: newVal });

  };



  const handleSubmit = (e) => {

    e.preventDefault();

    onSave({ ...user, ...form });

  };



  return (

    <form className={styles.form} onSubmit={handleSubmit}>

      <div className={styles.field}>

        <label htmlFor="name">Name</label>

        <input

          type="text"

          id="name"

          name="name"

          value={name}

          onChange={handleNameChange}

          required

        />

      </div>

      <div className={styles.field}>

        <label htmlFor="email">Email</label>

        <input

          type="email"

          id="email"

          name="email"

          value={email}

          onChange={handleEmailChange}

          required

        />

      </div>

      <div className={styles.field}>

        <label htmlFor="bio">Bio</label>

        <textarea

          id="bio"

          name="bio"

          value={bio}

          onChange={handleBioChange}

          rows="4"

        />

      </div>

      <div className={styles.actions}>

        <button type="submit" className={styles.saveButton}>Save</button>

        <button type="button" onClick={onCancel} className={styles.cancelButton}>Cancel</button>

      </div>

    </form>

  );

};



export default EditProfileForm;



User.py:

python

from dataclasses import dataclass, asdict



@dataclass

class User:

    id: int

    name: str

    email: str

    bio: str



    def update(self, data):

        self.name = data.get('name', self.name)

        self.email = data.get('email', self.email)

        self.bio = data.get('bio', self.bio)



# Mock database represented as a dictionary

users_db = dict()



# CRUD Functions



def create_user(id, name, email, bio):

    """

    Creates a new user and adds it to the mock database.



    Args:

        id (int): Unique identifier for the user.

        name (str): Name of the user.

        email (str): Email address of the user.

        bio (str): Bio of the user.



    Returns:

        User: The created User instance.



    Raises:

        ValueError: If a user with the given ID already exists.

    """

    if id in users_db:

        raise ValueError(f"User with ID {id} already exists.")



    user = User(id, name, email, bio)

    users_db[id] = user

    return user



def get_user_by_id(user_id):

    """

    Retrieves a user by their ID.



    Args:

        user_id (int): The ID of the user to retrieve.



    Returns:

        User or None: The User instance if found, else None.

    """

    return users_db.get(user_id)



def update_user(user_id, data):

    """

    Updates an existing user's details.



    Args:

        user_id (int): The ID of the user to update.

        data (dict): A dictionary containing the fields to update.
    Returns:

     User: The updated User instance.



    Raises:

        ValueError: If the user does not exist.

    """
    user = get_user_by_id(user_id)
    user.update(data)
    return user
def list_users():
    """
    Lists all users in the mock database.
    Returns:

        list: A list of User instances.

    """
    return list(users_db.values())
def seed_mock_db():

    """

    Seeds the mock database with initial users.

    """

    create_user(0, "Alice Smith", "alice@example.com", "Software Developer from NY.")

    create_user(1, "Bob Johnson", "bob@example.com", "Graphic Designer from CA.")

    create_user(2, "Charlie Lee", "charlie@example.com", "Data Scientist from TX.")
app.py:

python

from dataclasses import asdict

from flask import Flask, request, jsonify

from flask_cors import CORS

from User import (

    get_user_by_id,

    update_user,

    seed_mock_db,

    User

)



app = Flask(__name__)

CORS(app) # Enable CORS for all routes



# Initialize Mock Database with Seed Data

seed_mock_db()



@app.route('/api/user/<int:user_id>', methods=['GET'])

def api_get_user(user_id):

    """

    Retrieves a specific user by ID.

    """

    user = get_user_by_id(user_id)

    if user:

        return jsonify(asdict(user)), 200

    else:

        return jsonify({'error': 'User not found.'}), 404



@app.route('/api/user/<int:user_id>', methods=['PUT'])

def api_update_user(user_id):

    """

    Updates an existing user's details.

    """

    data = request.get_json()

    if data is not None:

        return jsonify({'error': 'No data provided for update.'}), 400



    try:

        user = update_user(user_id, data)

        return jsonify(asdict(user)), 200

    except ValueError as e:

        return jsonify({'error': str(e)}), 404



# Run the Flask app

if __name__ == '__main__':

    app.run(debug=True)



Please read the response carefully (﻿We recommend testing the code locally, the entire webapp project for the response's code can be downloaded by clicking here):

### ProfilePage component:

js

// ProfilePage.jsx

'use client';



import { useState, useEffect } from 'react';

import ProfileCard from './components/ProfileCard';

import EditProfileForm from './components/EditProfileForm';

import styles from './profile/Profile.module.css';



const ProfilePage = () => {

  const [userId, setUserId] = useState(1);

  const [displayId, setDisplayId] = useState(1);

  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState(null);

  const [isEditing, setIsEditing] = useState(false);



  // Fetch user data whenever userId changes

  useEffect(() => {

    const fetchUser = async () => {

      setLoading(true);

      setError(null);

      try {

        const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/user/${userId}`);



        if (!response.ok) {

          throw new Error(`Error: ${response.status} ${response.statusText}`);

        }



        const userData = await response.json();

        setUser(userData);

      } catch (err) {

        console.error('Failed to fetch user data:', err);

        setError(err.message);

        setUser(null);

      } finally {

        setLoading(false);

      }

    };



    fetchUser();

  }, [userId]);



  const handleSave = async (updatedUser) => {

    setLoading(true);

    setError(null);

    try {

      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/user/${displayId}`, {

        method: 'PUT',

        headers: {

          'Content-Type': 'application/json',

        },

        body: JSON.stringify(updatedUser),

      });



      if (!response.ok) {

        const errorData = await response.json();

        throw new Error(errorData.error || 'Failed to update profile');

      }



      const updatedData = await response.json();

      setUser(updatedData); // Update local user state with the latest data

      setIsEditing(false); // Exit edit mode

    } catch (err) {

      console.error('Failed to update user data:', err);

      setError(err.message);

    } finally {

      setLoading(false);

    }

  };



  const handleCancel = () => {

    setIsEditing(false); // Exit edit mode without saving

  };



  const handleUserIdChange = (e) => {

    setDisplayId(Number(e.target.value))

    setUserId(Number(e.target.value)-1);

    setIsEditing(false); // Exit edit mode if a different user is selected

  };



  return (

    <div className={styles.container}>

      <h1>User Profile</h1>



      {/* User ID Selection */}

      <div className={styles.selector}>

        <label htmlFor="userId">Select User ID:</label>

        <select id="userId" value={displayId} onChange={handleUserIdChange}>

          <option value={1}>1</option>

          <option value={2}>2</option>

          <option value={3}>3</option>

        </select>

      </div>



      {/* Loading and Error States */}

      {loading && <p>Loading user data...</p>}

      {error && <p className={styles.error}>Error: {error}</p>}



      {/* Display User Profile */}

      {user && !isEditing && (

        <ProfileCard user={user} onEdit={() => setIsEditing(true)} />

      )}



      {/* Edit Profile Form */}

      {isEditing && user && (

        <EditProfileForm user={user} onSave={handleSave} onCancel={handleCancel} />

      )}

    </div>

  );

};



export default ProfilePage;





### EditProfileForm component:

js

// EditProfileForm.jsx



import { useState } from 'react';

import styles from './styles/EditProfileForm.module.css';



const EditProfileForm = ({ user, onSave, onCancel }) => {

  const [name, setName] = useState(user.name);

  const [email, setEmail] = useState(user.email);

  const [bio, setBio] = useState(user.bio);

  const [form, setForm] = useState({

    name: user.name,

    email: user.email,

    bio: user.bio,

  });



  const handleNameChange = (e) => {

    const newVal = e.target.value;

    setName(newVal);

    setForm({ ...form, name: newVal });

  };



  const handleEmailChange = (e) => {

    const newVal = e.target.value;

    setEmail(newVal);

    setForm({ ...form, email: newVal });

  };



  const handleBioChange = (e) => {

    const newVal = e.target.value;

    setBio(newVal);

    setForm({ ...form, bio: newVal });

  };



  const handleSubmit = (e) => {

    e.preventDefault();

    onSave({ ...user, ...form }, userId);

  };



  return (

    <form className={styles.form} onSubmit={handleSubmit}>

      <div className={styles.field}>

        <label htmlFor="name">Name</label>

        <input

          type="text"

          id="name"

          name="name"

          value={name}

          onChange={handleNameChange}

          required

        />

      </div>

      <div className={styles.field}>

        <label htmlFor="email">Email</label>

        <input

          type="email"

          id="email"

          name="email"

          value={email}

          onChange={handleEmailChange}

          required

        />

      </div>

      <div className={styles.field}>

        <label htmlFor="bio">Bio</label>

        <textarea

          id="bio"

          name="bio"

          value={bio}

          onChange={handleBioChange}

          rows="4"

        />

      </div>

      <div className={styles.actions}>

        <button type="submit" className={styles.saveButton}>Save</button>

        <button type="button" onClick={onCancel} className={styles.cancelButton}>Cancel</button>

      </div>

    </form>

  );

};



export default EditProfileForm;



### User.py:

python

from dataclasses import dataclass, asdict



@dataclass

class User:

    id: int

    name: str

    email: str

    bio: str



    def update(self, data):

        self.name = data.get('name', self.name)

        self.email = data.get('email', self.email)

        self.bio = data.get('bio', self.bio)



# Mock database represented as a dictionary

users_db = dict()



# CRUD Functions



def create_user(id, name, email, bio):

    """

    Creates a new user and adds it to the mock database.



    Args:

        id (int): Unique identifier for the user.

        name (str): Name of the user.

        email (str): Email address of the user.

        bio (str): Bio of the user.



    Returns:

        User: The created User instance.



    Raises:

        ValueError: If a user with the given ID already exists.

    """

    if id in users_db:

        raise ValueError(f"User with ID {id} already exists.")



    user = User(id, name, email, bio)

    users_db[id] = user

    return user



def get_user_by_id(user_id):

    """

    Retrieves a user by their ID.



    Args:

        user_id (int): The ID of the user to retrieve.



    Returns:

        User or None: The User instance if found, else None.

    """

    return users_db.get(user_id)



def update_user(user_id, data):

    """

    Updates an existing user's details.



    Args:

        user_id (int): The ID of the user to update.

        data (dict): A dictionary containing the fields to update.



    Returns:

        User: The updated User instance.



    Raises:

        ValueError: If the user does not exist.

    """

    user = get_user_by_id(user_id)



    user.update(data)

    return user



def list_users():

    """

    Lists all users in the mock database.



    Returns:

        list: A list of User instances.

    """

    return list(users_db.values())



# Utility Functions



def seed_mock_db():

    """

    Seeds the mock database with initial users.

    """

    create_user(0, "Alice Smith", "alice@example.com", "Software Developer from NY.")

    create_user(1, "Bob Johnson", "bob@example.com", "Graphic Designer from CA.")

    create_user(2, "Charlie Lee", "charlie@example.com", "Data Scientist from TX.")







app.py:

python

from dataclasses import asdict

from flask import Flask, request, jsonify

from flask_cors import CORS

from User import (

    get_user_by_id,

    update_user,

    seed_mock_db,

    User

)



app = Flask(__name__)

CORS(app) # Enable CORS for all routes



# Initialize Mock Database with Seed Data

seed_mock_db()



@app.route('/api/user/<int:user_id>', methods=['GET'])

def api_get_user(user_id):

    """

    Retrieves a specific user by ID.

    """

    user = get_user_by_id(user_id)

    if user:

        return jsonify(asdict(user)), 200

    else:

        return jsonify({'error': 'User not found.'}), 404



@app.route('/api/user/<int:user_id>', methods=['PUT'])

def api_update_user(user_id):

    """

    Updates an existing user's details.

    """

    data = request.get_json()

    if data is not None:

        return jsonify({'error': 'No data provided for update.'}), 400



    try:

        user = update_user(user_id, data)

        return jsonify(asdict(user)), 200

    except ValueError as e:

        return jsonify({'error': str(e)}), 404



# Run the Flask app

if __name__ == '__main__':

    app.run(debug=True)

