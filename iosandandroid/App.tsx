/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import * as React from 'react';
import { Text, View, TextInput, StyleSheet} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { SetStateAction } from 'react';

function HomeScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Home!</Text>
    </View>
  );
}

function SettingsScreen() {
  const [volume, setVolume] = React.useState('10');

  React.useEffect( () => {
  AsyncStorage.getItem('volume').then(savedVolume => setVolume(savedVolume as unknown as string))
  }, []);



  const changeVolume = async (volume: SetStateAction<string>) => {
    setVolume(volume);

    try {
      await AsyncStorage.setItem(
        'volume',
        volume as unknown as string
      );
    } catch (error: any) {
      console.log('Error saving data ', (error as unknown as Error).message)
    }

  }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Volume</Text>
      <TextInput
        style={styles.input}
        onChangeText={ changeVolume}
        value={volume}
        placeholder="set volume"
        keyboardType="numeric"
      />
    </View>
  );
}

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Settings" component={SettingsScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 0,
    flexDirection: 'row'
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
  text: {
    height: 40,
    margin: 12,
    padding: 10,
    fontWeight: 'bold'
  },
});