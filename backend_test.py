#!/usr/bin/env python3
"""
Backend API Testing for Vietnamese Graduation Invitation Website
Tests all Friend Management and Graduation Information APIs
"""

import requests
import json
import uuid
from datetime import datetime
import sys
import os

# Get backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Error reading frontend .env: {e}")
        return None

BASE_URL = get_backend_url()
if not BASE_URL:
    print("ERROR: Could not get REACT_APP_BACKEND_URL from frontend/.env")
    sys.exit(1)

API_URL = f"{BASE_URL}/api"
print(f"Testing backend API at: {API_URL}")

class BackendTester:
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
        self.friend_ids = []
        
    def log_test(self, test_name, success, message="", data=None):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        self.test_results.append({
            'test': test_name,
            'success': success,
            'message': message,
            'data': data
        })
        
    def test_api_root(self):
        """Test API root endpoint"""
        try:
            response = self.session.get(f"{API_URL}/")
            if response.status_code == 200:
                data = response.json()
                if "message" in data:
                    self.log_test("API Root", True, f"API accessible: {data['message']}")
                    return True
                else:
                    self.log_test("API Root", False, "Missing message in response")
                    return False
            else:
                self.log_test("API Root", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("API Root", False, f"Connection error: {str(e)}")
            return False
    
    def test_init_data(self):
        """Test POST /api/init-data endpoint"""
        try:
            response = self.session.post(f"{API_URL}/init-data")
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "initialized" in data["message"]:
                    self.log_test("Initialize Sample Data", True, "Sample friends initialized successfully")
                    return True
                else:
                    self.log_test("Initialize Sample Data", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("Initialize Sample Data", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Initialize Sample Data", False, f"Error: {str(e)}")
            return False
    
    def test_get_friends(self):
        """Test GET /api/friends endpoint"""
        try:
            response = self.session.get(f"{API_URL}/friends")
            if response.status_code == 200:
                friends = response.json()
                if isinstance(friends, list):
                    # Check for expected sample friends
                    friend_names = [f.get('name', '') for f in friends]
                    expected_names = ["Ha Nguyen Tuan Kiet", "Vu Van Hau"]
                    
                    # Store friend IDs for later tests
                    self.friend_ids = [f.get('id') for f in friends if f.get('id')]
                    
                    if len(friends) >= 2:
                        found_names = [name for name in expected_names if name in friend_names]
                        if len(found_names) == 2:
                            self.log_test("Get Friends List", True, f"Found {len(friends)} friends including expected Vietnamese names")
                            
                            # Validate friend structure
                            for friend in friends:
                                if not all(key in friend for key in ['id', 'name', 'created_at']):
                                    self.log_test("Friend Data Structure", False, "Missing required fields in friend object")
                                    return False
                                    
                                # Validate UUID format
                                try:
                                    uuid.UUID(friend['id'])
                                except ValueError:
                                    self.log_test("Friend UUID Validation", False, f"Invalid UUID format: {friend['id']}")
                                    return False
                            
                            self.log_test("Friend Data Structure", True, "All friends have valid structure and UUIDs")
                            return True
                        else:
                            self.log_test("Get Friends List", False, f"Expected Vietnamese names not found. Found: {friend_names}")
                            return False
                    else:
                        self.log_test("Get Friends List", False, f"Expected at least 2 friends, got {len(friends)}")
                        return False
                else:
                    self.log_test("Get Friends List", False, "Response is not a list")
                    return False
            else:
                self.log_test("Get Friends List", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Get Friends List", False, f"Error: {str(e)}")
            return False
    
    def test_get_friend_by_id(self):
        """Test GET /api/friends/{friend_id} endpoint"""
        if not self.friend_ids:
            self.log_test("Get Friend by ID", False, "No friend IDs available for testing")
            return False
            
        try:
            # Test with valid friend ID
            friend_id = self.friend_ids[0]
            response = self.session.get(f"{API_URL}/friends/{friend_id}")
            
            if response.status_code == 200:
                friend = response.json()
                if all(key in friend for key in ['id', 'name', 'created_at']):
                    if friend['id'] == friend_id:
                        self.log_test("Get Friend by ID", True, f"Successfully retrieved friend: {friend['name']}")
                        
                        # Test with invalid friend ID
                        invalid_id = str(uuid.uuid4())
                        response = self.session.get(f"{API_URL}/friends/{invalid_id}")
                        if response.status_code == 404:
                            self.log_test("Get Friend by Invalid ID", True, "Correctly returns 404 for non-existent friend")
                            return True
                        else:
                            self.log_test("Get Friend by Invalid ID", False, f"Expected 404, got {response.status_code}")
                            return False
                    else:
                        self.log_test("Get Friend by ID", False, "Returned friend ID doesn't match requested ID")
                        return False
                else:
                    self.log_test("Get Friend by ID", False, "Missing required fields in friend response")
                    return False
            else:
                self.log_test("Get Friend by ID", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Get Friend by ID", False, f"Error: {str(e)}")
            return False
    
    def test_create_friend(self):
        """Test POST /api/friends endpoint"""
        try:
            # Test creating a new friend with Vietnamese name
            new_friend_data = {
                "name": "Nguyễn Thị Mai Anh"
            }
            
            response = self.session.post(f"{API_URL}/friends", json=new_friend_data)
            
            if response.status_code == 200:
                friend = response.json()
                if all(key in friend for key in ['id', 'name', 'created_at']):
                    if friend['name'] == new_friend_data['name']:
                        # Validate UUID
                        try:
                            uuid.UUID(friend['id'])
                            self.log_test("Create Friend", True, f"Successfully created friend: {friend['name']} with ID: {friend['id']}")
                            
                            # Verify the friend was actually saved by retrieving it
                            get_response = self.session.get(f"{API_URL}/friends/{friend['id']}")
                            if get_response.status_code == 200:
                                retrieved_friend = get_response.json()
                                if retrieved_friend['name'] == new_friend_data['name']:
                                    self.log_test("Friend Persistence", True, "Created friend persisted correctly in database")
                                    return True
                                else:
                                    self.log_test("Friend Persistence", False, "Created friend data doesn't match when retrieved")
                                    return False
                            else:
                                self.log_test("Friend Persistence", False, "Could not retrieve created friend")
                                return False
                        except ValueError:
                            self.log_test("Create Friend", False, f"Invalid UUID in response: {friend['id']}")
                            return False
                    else:
                        self.log_test("Create Friend", False, "Response name doesn't match input")
                        return False
                else:
                    self.log_test("Create Friend", False, "Missing required fields in response")
                    return False
            else:
                self.log_test("Create Friend", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Create Friend", False, f"Error: {str(e)}")
            return False
    
    def test_graduation_info(self):
        """Test GET /api/graduation-info endpoint"""
        try:
            response = self.session.get(f"{API_URL}/graduation-info")
            
            if response.status_code == 200:
                grad_info = response.json()
                
                # Check required fields
                required_fields = ['graduate_name', 'major', 'university', 'date', 'time', 'location', 'address']
                missing_fields = [field for field in required_fields if field not in grad_info]
                
                if missing_fields:
                    self.log_test("Graduation Info Structure", False, f"Missing fields: {missing_fields}")
                    return False
                
                # Validate specific Vietnamese content
                expected_values = {
                    'graduate_name': 'Nguyen Van Tuyen',
                    'date': '19/8/2025',
                    'time': '08:00',
                    'university': 'FPT University'
                }
                
                validation_errors = []
                for key, expected_value in expected_values.items():
                    if grad_info.get(key) != expected_value:
                        validation_errors.append(f"{key}: expected '{expected_value}', got '{grad_info.get(key)}'")
                
                if validation_errors:
                    self.log_test("Graduation Info Content", False, f"Content validation errors: {'; '.join(validation_errors)}")
                    return False
                
                # Check Vietnamese text handling
                vietnamese_fields = ['major', 'address']
                has_vietnamese = any('ệ' in str(grad_info.get(field, '')) or 'ư' in str(grad_info.get(field, '')) or 'ă' in str(grad_info.get(field, '')) 
                                   for field in vietnamese_fields)
                
                if has_vietnamese:
                    self.log_test("Vietnamese Text Support", True, "Vietnamese characters properly handled")
                else:
                    self.log_test("Vietnamese Text Support", False, "No Vietnamese characters found in expected fields")
                
                self.log_test("Graduation Info", True, f"All graduation details correct for {grad_info['graduate_name']}")
                return True
                
            else:
                self.log_test("Graduation Info", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Graduation Info", False, f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all backend tests in sequence"""
        print("=" * 60)
        print("VIETNAMESE GRADUATION INVITATION - BACKEND API TESTS")
        print("=" * 60)
        
        tests = [
            ("API Connectivity", self.test_api_root),
            ("Initialize Sample Data", self.test_init_data),
            ("Friend Management - List", self.test_get_friends),
            ("Friend Management - Get by ID", self.test_get_friend_by_id),
            ("Friend Management - Create", self.test_create_friend),
            ("Graduation Information", self.test_graduation_info),
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            print(f"\n--- Testing {test_name} ---")
            if test_func():
                passed += 1
            print()
        
        print("=" * 60)
        print(f"BACKEND TEST SUMMARY: {passed}/{total} tests passed")
        print("=" * 60)
        
        # Print detailed results
        print("\nDETAILED RESULTS:")
        for result in self.test_results:
            status = "✅" if result['success'] else "❌"
            print(f"{status} {result['test']}: {result['message']}")
        
        return passed == total

if __name__ == "__main__":
    tester = BackendTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)