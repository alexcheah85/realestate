import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { motion } from 'framer-motion';

const initialProperties = [
  { id: 1, title: 'Modern Condo in KLCC', location: 'Kuala Lumpur', price: 'RM 1,200,000', description: 'A luxurious condo in the heart of KLCC with stunning views.', images: ['https://via.placeholder.com/300'] },
  { id: 2, title: 'Beachfront Villa in Penang', location: 'Penang', price: 'RM 2,800,000', description: 'Exclusive beachfront villa offering privacy and luxury.', images: ['https://via.placeholder.com/300'] },
  { id: 3, title: 'Bungalow in Ipoh', location: 'Perak', price: 'RM 980,000', description: 'Spacious bungalow located in a serene environment.', images: ['https://via.placeholder.com/300'] },
];

const RealEstateApp = () => {
  const [properties, setProperties] = useState(initialProperties);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedProperty, setSelectedProperty] = useState(null);
  const [isAddingProperty, setIsAddingProperty] = useState(false);

  const filteredProperties = properties.filter(property =>
    property.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    property.location.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleAddProperty = (e) => {
    e.preventDefault();
    const newProperty = {
      id: properties.length + 1,
      title: e.target.title.value,
      location: e.target.location.value,
      price: e.target.price.value,
      description: e.target.description.value,
      images: ['https://via.placeholder.com/300'],
    };
    setProperties([...properties, newProperty]);
    setIsAddingProperty(false);
  };

  return (
    <div className="p-4">
      <h1 className="text-3xl font-bold mb-4">ARISE Real Estate Listings</h1>
      {isAddingProperty ? (
        <form onSubmit={handleAddProperty} className="mb-4">
          <Input name="title" placeholder="Property Title" className="mb-2" required />
          <Input name="location" placeholder="Location" className="mb-2" required />
          <Input name="price" placeholder="Price" className="mb-2" required />
          <Input name="description" placeholder="Description" className="mb-2" required />
          <Button type="submit" className="mr-2">Add Property</Button>
          <Button type="button" onClick={() => setIsAddingProperty(false)}>Cancel</Button>
        </form>
      ) : selectedProperty ? (
        <div>
          <Button className="mb-4" onClick={() => setSelectedProperty(null)}>Back to Listings</Button>
          <h2 className="text-2xl font-bold">{selectedProperty.title}</h2>
          <img src={selectedProperty.images[0]} alt={selectedProperty.title} className="w-full h-64 object-cover rounded-xl" />
          <p>{selectedProperty.description}</p>
          <p className="text-red-600 font-bold">{selectedProperty.price}</p>
          <p className="font-bold">Location: {selectedProperty.location}</p>
        </div>
      ) : (
        <>
          <div className="mb-4">
            <Input
              placeholder="Search properties..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="mb-4"
            />
            <Button onClick={() => setIsAddingProperty(true)} className="mb-4">Add New Property</Button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {filteredProperties.map(property => (
              <motion.div
                key={property.id}
                whileHover={{ scale: 1.05 }}
              >
                <Card className="rounded-2xl shadow-lg">
                  <CardContent>
                    <img src={property.images[0]} alt={property.title} className="w-full h-48 object-cover rounded-xl" />
                    <h2 className="text-xl font-bold mt-2">{property.title}</h2>
                    <p>{property.location}</p>
                    <p className="text-red-600 font-bold">{property.price}</p>
                    <Button className="mt-2" onClick={() => setSelectedProperty(property)}>View Details</Button>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default RealEstateApp;
