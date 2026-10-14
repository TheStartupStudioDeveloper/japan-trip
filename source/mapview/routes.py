# Hand-checked Google Maps routes by place name, per day. Each: (button label, origin, destination, [waypoints], travel mode).
# Google Maps takes up to 10 stops per link, and transit only between two points, so train legs get their own link.
ROUTES = {
 17: [
  ('Narita Airport to Shibuya, by train', 'Narita International Airport Terminal 2', 'Shibuya Station', [], 'transit'),
  ('Shibuya walking day, all 10 stops', 'Hachiko Memorial Statue, Shibuya', 'Nonbei Yokocho, Shibuya',
   ['sequence MIYASHITA PARK, Shibuya', 'MIYASHITA PARK, Shibuya', 'Cat Street, Jingumae, Shibuya', 'Omotesando Hills',
    'Shibuya Scramble Crossing', 'MEGA Don Quijote Shibuya Honten', 'sequence MIYASHITA PARK, Shibuya', 'SHIBUYA SKY'], 'walking'),
 ],
}
