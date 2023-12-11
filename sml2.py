from sklearn.model_selection import train_test_split

# Load the dataset - replace 'donations.csv' with the actual file name or path
df = pd.read_csv('donations.csv')

# Convert 'Date Donated' to datetime format
df['Date Donated'] = pd.to_datetime(df['Date Donated'])

# Extract month from the date and use it as a feature
df['Month'] = df['Date Donated'].dt.month

# Select the feature and target variable for linear regression
X = df[['Month']]  # Feature (Month)
y = df['Amount']  # Target variable

# Split the data into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add a column of 1s to the features to represent the intercept term for both train and test sets
X_train['Intercept'] = 1
X_test['Intercept'] = 1

# Convert the data to matrices for easier matrix operations
X_train = X_train.to_numpy()
X_test = X_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

# The rest of the code (calculating coefficients, predicting, R-squared, and plotting) remains the same.
# It should be performed separately for the training and testing sets to assess the model's performance on unseen data.
