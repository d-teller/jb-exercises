-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO users (name, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Bob Johnson', 'bob@example.com')
ON CONFLICT (email) DO NOTHING;

-- Create sessions table for user activity
CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    session_start TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    session_end TIMESTAMP WITH TIME ZONE,
    ip_address VARCHAR(45),
    user_agent TEXT
);

-- Create function to record session end times
CREATE OR REPLACE FUNCTION update_session_end()
RETURNS TRIGGER AS $$
BEGIN
    NEW.session_end = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for session end times
CREATE TRIGGER set_session_end
BEFORE UPDATE ON sessions
FOR EACH ROW
EXECUTE FUNCTION update_session_end();

-- Create index on user_id for faster lookups
CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);