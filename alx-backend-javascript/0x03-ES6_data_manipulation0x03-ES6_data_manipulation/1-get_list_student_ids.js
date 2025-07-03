/**
 * Retrieves a list of student IDs.
 * @param {Array} students - An array of student objects.
 * @returns {Array} An array of student IDs.
 */
export default function getListStudentIds(students) {
  if (students instanceof Array) {
    return students.map((student) => student.id);
  }
  return [];
}
